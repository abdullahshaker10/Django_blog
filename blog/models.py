# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
import string
import random
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.db.models import Q, Count, F, Sum, Avg, Max
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from .signals import object_viewed_signal

from PIL import Image
from itertools import chain
from datetime import date

from user.models import *
import pdb

# User = settings.AUTH_USER_MODEL
User = get_user_model()


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, null=True, blank=True)
    post_image = models.ImageField(
        default='post_default.jpg', upload_to='images')
    content = models.TextField()
    post_publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    price = models.IntegerField(default=5)
    time_to_deliver = models.IntegerField(default=3)

    def __str__(self):
        return self.title

    def get_post_rate(self):
        reviews = Comment.objects.filter(
            post=self, parent__isnull=True).aggregate(post_av_rating=Avg('rating'))
        avg = 0
        if reviews['post_av_rating'] is not None:
            avg = float(reviews['post_av_rating'])
        return avg

    def get_absolute_url(self):
        return reverse('detail-post', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        app_label = "blog"
        ordering = ('-post_publish',)

    @property
    def has_coupon(self):
        try:
            return self.coupon
        except:
            return False

    @property
    def is_coupon_valid(self):
        return True if self.coupon.is_usable else False

    @property
    def discount_price(self):
        if self.has_coupon and self.is_coupon_valid:
            _category = self.coupon.category
            discount = self.coupon.discount
            return (self.price) * (discount / 100) if _category == "P" else (int(discount))
        return None

    @property
    def price_after_discount(self):
        return self.price - int(self.discount_price)

    @property
    def site_commission_calc(self):
        if self.price <= 50:
            commission = 2
        else:
            commission = (self.price * 5) / 100
        return int(commission)

    @property
    def final_price_with_discount(self):
        if self.has_coupon and self.is_coupon_valid:
            total_price = self.price_after_discount + self.site_commission_calc
            return int(total_price)

    @property
    def final_price_without_discount(self):
            total_price = self.price + self.site_commission_calc
            return int(total_price)

    # @property
    # def final_price(self):
    #     return self.price + self.site_commission_calc


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter')
    content = models.TextField(verbose_name='Comment')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    rating = models.FloatField(default=1, null=True, blank=True)

    def __str__(self):
        return '{} Commented On {}.'.format(self.user, self.post)

    class Meta:
        app_label = "blog"
        ordering = ('-comment_date',)



class Order(models.Model):
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orderbuyer')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='orderpost')
    order_created = models.DateTimeField(auto_now_add=True)
    state = models.CharField(
        max_length=50,
        default='Pending'
    )
    final_price = models.IntegerField(default=5)
    final_date_to_deliver = models.DateTimeField(null=True)

    def __str__(self):
        return 'User ( {} ) Ordered ( {} ).'.format(self.buyer, self.post)


def get_random_code(length=8):
    random_code = ''.join(random.SystemRandom().choice(
        string.ascii_uppercase + string.digits) for _ in range(length))
    site_string = 'HALA-'
    return "".join((site_string, random_code))


class Coupon(models.Model):
    COUPON_TYPES = (
        (None, "Select coupon type"),
        ("P", "Percentage based-coupon"),
        ("A", "Amount based-coupon")
    )
    post = models.OneToOneField(
        Post, on_delete=models.CASCADE, related_name='coupon')
    code = models.CharField(max_length=8, default=get_random_code,
                            verbose_name="Coupon Code", unique=True, editable=False)
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.CharField(
        "Coupon Type",
        max_length=1,
        default="P",
        choices=COUPON_TYPES
    )
    discount = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        help_text="Provide percentage value e.g 20 for percentage-based coupon \
            or amount e.g 2400 for amount-based coupon"
    )
    usage = models.IntegerField(
        "Coupon Usage(optional)",
        null=True, blank=True,
        help_text="Provide the number this coupon can be used or leave \
            this field empty for unlimited usage"
    )
    is_activated = models.BooleanField("Activation Status", default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="coupons")

    class Meta:
        db_table = "coupons"
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"
        ordering = ("-created_at",)

    def __str__(self):
        return str(self.code)

    @property
    def is_unlimited(self):
        return False if self.usage else True

    @property
    def is_expired(self):
        today = date.today()
        return True if self.end_date < today else False

    @property
    def is_usable(self):
        return True if not self.is_expired and self.is_activated else False

    def coupon(self):
        return self.code


class CouponOrder(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, null=True, on_delete=models.SET_NULL)

    is_complete = models.BooleanField(
        "Order Completion", default=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")

    class Meta:
        db_table = "coupon_orders"
        verbose_name = "coupon_orders"
        verbose_name_plural = "Coupon Orders"
        ordering = ("-created_at",)

    def __str__(self):
        return self.created_by.username

    def price(self):
        old_price = self.post.price
        if self.coupon:
            _category = self.coupon.category
            discount = self.coupon.discount
            return (old_price * discount) / 100 if _category == "P" else (old_price - discount)
        return old_price
