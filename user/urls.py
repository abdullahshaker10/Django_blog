from django.urls import path
from django.conf.urls import url

from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('profile_update/', profile_update, name='profile_update'),
    path('users/', UserListView.as_view(), name='user_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
