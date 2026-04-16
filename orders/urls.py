from django.urls import path
from .views import CouponValidationView

urlpatterns = [
    path('coupon/validate',CouponValidationView.as_view(),name='coupon-validation'),
]