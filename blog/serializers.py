from rest_framework import serializers
from .models import Post, Coupon, Order


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    coupon = CouponSerializer(required=True)
    final_price_without_discount = serializers.ReadOnlyField()
    final_price_with_discount = serializers.ReadOnlyField()
    price_after_discount = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = '__all__'


class OrdderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

