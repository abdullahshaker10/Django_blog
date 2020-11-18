from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
# Create your views here.
from .models import Notification
from rest_framework.generics import ListAPIView
from .serializers import NotificationSerializer
from rest_framework.generics import DestroyAPIView

class NotificationListCBV(ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        query = Notification.objects.filter(
            seller=self.request.user).order_by('-creation_date')
        return query

class NotificationDeleteCBV(DestroyAPIView):
    queryset = Notification.objects.all()
    lookup_field = 'pk'
    
def mark_notification_as_readed(request):
    if not request.method == 'POST':
        return JsonResponse({})
    if not request.user.is_authenticated:
        return JsonResponse({})
    notifications = request.user.assigned_notifications
    unreaded_notifications = notifications.filter(is_read=False)
    for notification in unreaded_notifications.order_by('creation_date'):
        notification.is_read = True
        notification.save()
    return JsonResponse({'unreaded_notification_count': unreaded_notifications.count()})
