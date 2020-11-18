from django.contrib import admin

from .models import *
from .actions import activate_coupon


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post_publish', 'author',
                    'price', 'status', )
    list_filter = ('post_publish', 'status')
    search_fields = ('author__username', 'title', 'content')
    list_editable = ('status', 'price',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Order)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ["post", "coupon", "is_activated"]
    list_filter = ["is_activated"]
    search_fields = ["post__title", "create_by__username"]
    list_editable = ('is_activated',)
    actions = [activate_coupon]


@admin.register(CouponOrder)
class CouponOrderAdmin(admin.ModelAdmin):
    list_display = [
        "post",
        "created_by",
        "coupon",
        "price",
        "is_complete"
    ]
    search_fields = ["created_by__username"]
    list_filter = ["is_complete"]
