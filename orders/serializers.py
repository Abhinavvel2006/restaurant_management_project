from rest_framework import serializers
from .models import Coupon

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        models=Coupon
        fields = ['code','discount_percentage']
        