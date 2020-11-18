import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.core import serializers
from channels.generic.websocket import AsyncJsonWebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from .serializers import NotificationSerializer
from json import dumps


class NotificationConsumer(AsyncJsonWebsocketConsumer):

    async def websocket_connect(self, event):
        print("CONNECTED", event)

        await self.channel_layer.group_add(
            f"notification_group_{self.scope['url_route']['kwargs']['user_id']}",
            self.channel_name
        )

        await self.accept()

        context = await self.get_notification_info(self.scope)

        await self.send_json(content=context)

    async def websocket_disconnect(self, event):
        print("DISCONNECTED", event)

    async def websocket_receive(self, event):
        print("RECEIVE", event)

    async def notification_info(self, event):
        context = await self.get_notification_info(self.scope)

        await self.send_json(content=context)

    @database_sync_to_async
    def get_notification_info(self, scope):

        notification = scope['user'].assigned_notifications.last()
        if notification is not None:
            post = notification.order.post.title
            buyer = notification.buyer.username
            message = f"{buyer} ordered {post}"
            order = notification.order.id
            has_notification = True
            notification_id = notification.id
        else:
            has_notification = False
            message = None
            order = None
            notification_id = None

        context = {
            'has_notification': has_notification,
            'notification': message,
            'order': order,
            'notification_id': notification_id
        }

        return context


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("chat CONNECTED")

        self.room_name = self.scope['url_route']['kwargs']['order_id']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        print("chat DISCONNECTED", event)

    # Receive message from WebSocket

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
