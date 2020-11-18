from django.db.models import Count, F, Sum, Q
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from user.forms import UserCreationForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from blog.models import *
from user.models import *


def extra_free_cp(request, category_slug=None):
    orders = Order.objects.all()
    posts = Post.objects.all()

    context = {
        'orders': orders,
        'posts': posts,
    }
    return context

