from django.db import models
from django.contrib.auth import get_user_model
from blog.models import Order
User = get_user_model()


class Notification(models.Model):
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='assigned_notifications')
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sender_notifications', null=True)
    body = models.TextField(max_length=50, default='NO description')
    creation_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='notification', null=True)

    def __str__(self):
        return f"For: {self.seller}"
