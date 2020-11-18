import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from Notification.consumers import NotificationConsumer, ChatConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_blog.settings')

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                url(r"^ws/notification/(?P<user_id>\w+)/$",
                    NotificationConsumer.as_asgi()),
                url(r"^ws/chat/(?P<order_id>\w+)/$",
                    ChatConsumer.as_asgi()),

            ])

        )

    )
})
