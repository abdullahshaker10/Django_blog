from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView

from common.context_processors import *

User = get_user_model()


class UserDetailView(DetailView):
    template_name = 'user/user-details.html'
    model = User
    paginate_by = 10

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['coupons_history'] = CouponOrder.objects.filter(created_by=self.object)
        context['sell'] = Order.objects.all().filter(post__author=self.object).order_by('order_created')
       
        return context

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            messages.success(
                request, f'( Congratulations {new_user} .. You are now one of our community.')
            return redirect('login')
    else:
        form = UserCreationForm
    return render(request, 'user/register.html', {
        'form': form,
    })


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
        else:
            messages.warning(
                request, 'There is error in username or password .. please try again')
    return render(request, 'user/login.html', {})


def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html', {})


@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(
                request, 'Congratulations .. Your profile had been updated successfully')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form}

    return render(request, 'user/profile_update.html', context)


class UserListView(ListView):
    model = Profile
    template_name = 'user/users_list.html'
    context_object_name = 'users'
    # ordering = '-post_publish'
    paginate_by = 10


