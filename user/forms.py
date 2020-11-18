from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(
        label='Username',
        max_length=30,
        help_text='username should not contain spaces',
        widget=forms.TextInput(
            attrs={
                "id": "username"
            }
        )
    )
    email = forms.EmailField(label='E-Mail')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(
        label='Password Confirmation', widget=forms.PasswordInput(), min_length=8)
    gender = forms.ChoiceField(choices=Profile.GENDER_CHOICES)
    bio = forms.CharField(label='Bio', widget=forms.Textarea,
                          help_text='Type brief of yourself (Job, Certifications, Positions, .......)', )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2', 'gender', 'bio')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password doesnt match password confirmation')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('Username is exist .. Please try another username')
        return cd['username']


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='E-Mail')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
