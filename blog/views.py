import json
from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.html import strip_tags
from django.views.generic import DetailView, UpdateView, DeleteView, View, ListView, TemplateView, FormView
from django import template
from rest_framework.response import Response
from user.models import *
from .serializers import *
from .forms import *
from .mixins import *
from .models import *
from rest_framework.generics import RetrieveUpdateAPIView
from Notification.models import Notification
User = get_user_model()


# User = settings.AUTH_USER_MODEL


class PostListCBV(ListView):
    model = Post
    template_name = 'blog/Posts_List.html'
    context_object_name = 'posts'
    ordering = '-post_publish'
    paginate_by = 10


class PostDetailsCBV(ObjectViewMixin, DetailView):
    template_name = 'blog/Post_Details.html'
    form_class = CommentCreateForm
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailsCBV, self).get_context_data(**kwargs)
        post = Post.objects.get(slug=self.kwargs['slug'])
        context['comment_form'] = CommentCreateForm
        context['comments'] = Comment.objects.filter(
            post=self.get_object(), parent__isnull=True)
        return context

    def post(self, request, *args, **kwargs):
        _object = self.get_object()
        form = self.form_class(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            parent_id = request.POST.get('comment_id')
            comment_qs = None
            if parent_id:
                comment_qs = Comment.objects.get(id=parent_id)
            comment.parent = comment_qs
            comment.post = _object
            comment.save()
            if comment is not None:
                messages.success(request, "Comment successfully saved")
                return redirect(reverse("detail-post", kwargs={"slug": _object.slug}))

        return render(request, self.template_name, {
            "object": _object,
            "comment_form": form,
        })


class PostCreateView(LoginRequiredMixin, View):
    template_name = "blog/Post_Create.html"
    form_class = PostCreateForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "form": self.form_class
        })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            if post is not None:
                # send email to user to notify about new post
                _user_email = request.user.email
                _from_email = "weschoolinsight@gmail.com"
                subject = "New Post Created"
                post_link = reverse("detail-post", kwargs={"slug": post.slug})
                link = request.build_absolute_uri(post_link)
                msg_html = render_to_string(
                    "_email/post_layout.html",
                    {
                        "link": link,
                        "title": "Your post has been created"
                    }
                )
                msg_plain = strip_tags(msg_html)
                send_mail(
                    subject,
                    msg_plain,
                    _from_email,
                    [_user_email],
                    html_message=msg_html,
                    fail_silently=True
                )

                messages.success(
                    request, "Your post has been saved successfully.")
                return redirect(reverse("detail-post", kwargs={"slug": post.slug}))

        messages.error(
            request, "An error occured when saving your post.Please try again")
        return render(request, self.template_name, {
            "form": form
        })


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        _user_email = self.request.user.email
        _from_email = "weschoolinsight@gmail.com"
        subject = "Your post has been updated"
        _object = self.get_object()
        post_link = reverse("detail-post", kwargs={"slug": _object.slug})
        link = self.request.build_absolute_uri()
        msg_html = render_to_string(
            "_email/post_layout.html",
            {
                "link": link,
                "title": "Your post has been updated"
            }
        )
        msg_plain = strip_tags(msg_html)
        send_mail(
            subject,
            msg_plain,
            _from_email,
            [_user_email],
            html_message=msg_html,
            fail_silently=True
        )
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class HomePageCBV(TemplateView):
    template_name = "blog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_block_list = ['Slider01', 'Site Content 01']

        context['posts'] = Post.objects.all()
        context['profiles'] = Profile.objects.all()
        return context


# Emails System
def create_link(request):
    # print(request.get_full_path())
    link = request.build_absolute_uri(request.get_full_path())
    print(link)
    return render(request, "_email/post_layout.html")


# Coupon System
class CreateCouponView(DetailView):
    template_name = "coupons/create_coupon.html"
    form_class = CouponForm
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        _object = self.get_object()
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                coupon = form.save(commit=False)
                coupon.post = _object
                coupon.created_by = request.user
                coupon.save()

                if coupon is not None:
                    messages.success(request, "New coupon for {} post has been created successfully.\
                        ".format(_object.title))
                    return redirect(reverse("detail-post", kwargs={"slug": _object.slug}))
            except IntegrityError:
                messages.error(
                    request, "An error occurred, One coupon can be used for one post only")
                return redirect(reverse("detail-post", kwargs={"slug": _object.slug}))

        messages.error(
            request, "An error occurred when creating new coupon.Please try again")
        return render(request, self.template_name, {
            "form": form,
            "object": _object
        })


# Payment System
class CheckOutCBV(LoginRequiredMixin, FormView):
    form_class = CheckCouponForm
    template_name = 'payment/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        postId = self.kwargs['pk']
        post = Post.objects.get(id=postId)
        post.coupon_state = False
        post.save()
        context["post"] = post
        return context


# Payment System
@login_required(login_url='login')
def PaymentCompleteView(request):
    body = json.loads(request.body)
    post = Post.objects.get(id=body['postId'])
    final_price = body['finalPrice']
    # seller = Post.objects.get(author=post.author)
    Order.objects.create(
        post=post,
        buyer=request.user,
        final_price=final_price
    )
    return JsonResponse('Payment completed!', safe=False)


class PostApi(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        body = json.loads(request.body)
        instance.coupon_state = body['state']
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class OrderActionCBV(DetailView):
    def get(self, request, *args, **kwargs):
        order_id = self.kwargs['pk']
        order = Order.objects.get(id=order_id)
        action = self.kwargs['action']
        if action == 'accept':
            order.state = 'Accepted'
            current_date = datetime.now()
            new_date = current_date + timedelta(order.post.time_to_deliver)
            order.final_date_to_deliver = new_date
            order.save()

        else:
            order.state = 'Rejected'
            order.save()
        user_id = self.request.user.id
        return redirect(reverse('user-detail', kwargs={"pk": user_id}))


class OrderApiCBV(RetrieveUpdateAPIView):
    serializer_class = OrdderSerializer
    lookup_field = 'pk'
    queryset = Order.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        body = json.loads(request.body)
        if 'notificationId' in body:
            notification_id = body['notificationId']
            notification = Notification.objects.get(id=notification_id)
            notification.delete()

        if  body['action'] == 'Accepted':
            current_date = datetime.now()
            new_date = current_date + timedelta(instance.post.time_to_deliver)
            instance.final_date_to_deliver = new_date


        instance.state = body['action']
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)




register = template.Library()
