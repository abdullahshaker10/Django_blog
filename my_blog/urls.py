from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('user.urls')),
    path('', include('Notification.urls')),


    path('oauth/', include('social_django.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),

]
