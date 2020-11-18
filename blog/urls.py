from django.urls import path
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from .views import *

urlpatterns = [
    path('', HomePageCBV.as_view(), name='home'),

    path('project_list/', PostListCBV.as_view(), name='list-post'),
    path('project_create/', PostCreateView.as_view(), name='create-post'),
    path('project/<str:slug>/', PostDetailsCBV.as_view(), name='detail-post'),
    path('project/<slug:pk>/update/',
         PostUpdateView.as_view(), name='update-post'),
    path('project/<slug:pk>/delete/',
         PostDeleteView.as_view(), name='delete-post'),

    path("bogus/", create_link, name="create_link"),

    path('payment/checkout/<int:pk>',
         CheckOutCBV.as_view(), name="checkout"),
    path('payment/complete/', PaymentCompleteView, name="payment_complete"),

    path("coupon/add/<int:pk>/", CreateCouponView.as_view(), name="create"),
    path('api/post/<int:pk>', PostApi.as_view(), name='dispatchhistoryitem'),
    path('order/<int:pk>/<str:action>',OrderActionCBV.as_view(), name='order_action'),
     path('api/order/<int:pk>',OrderApiCBV.as_view())

]
