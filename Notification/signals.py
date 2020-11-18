from django.dispatch import receiver
from django.db.models.signals import post_save
from blog.models import Order
from .models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver(post_save, sender=Order)
def create_notification(*args, **kwargs):
    if kwargs['created']:
        order = kwargs['instance']
        if order.buyer != order.post.author:
            Notification.objects.create(
                seller=order.post.author, buyer=order.buyer, body=f"{order.buyer.username} ordered {order.post.title}", order=order)


@receiver(post_save, sender=Notification)
def send_notification_info(*args, **kwargs):
    if kwargs['created']:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"notification_group_{kwargs['instance'].seller.id}", {
                'type': 'notification_info'
            }
        )
