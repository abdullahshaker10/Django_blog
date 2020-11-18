from rest_framework import serializers
from .models import Notification
from blog.serializers import PostSerializer


class NotificationSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = Notification
        fields = '__all__'
