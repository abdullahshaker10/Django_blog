from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    list_display = ('__str__','id', 'is_read', 'body', 'seller', 'buyer')


admin.site.register(Notification, NotificationAdmin)
