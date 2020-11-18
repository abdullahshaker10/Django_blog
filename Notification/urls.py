from django.urls import path

from . import views

urlpatterns = [
    path(
        'ajax/mark_notification_as_readed',
        views.mark_notification_as_readed,
        name='AJAXMarkNotificationAsReaded'),
    path(
        'notifications/list', views.NotificationListCBV.as_view(), name='list_notifications'
    ),
    path(
        'notifications/delete/<int:pk>', views.NotificationDeleteCBV.as_view(), name='delete_notifications'
    )

]
