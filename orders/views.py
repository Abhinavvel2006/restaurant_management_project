from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from  django.utils.timezone import now
from .models import Coupon

class CouponValidationView(APIView):
    def post(self, request):
        code = request.data.get('code')

        if not code:
            return Response(
                {'error': 'Coupon code is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            coupon =Coupon.objects.get(code=code)
        except Coupon.DoesNotExist:
            return Response(
                {'error': 'Invalid coupon code.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        today = now().date()

        if not coupon.is_active:
            return Response(
                {'error': 'This coupon is inactive.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if today < coupon.valid_from or today > coupon.valid_until:
            return Response(
                {'error':'This coupon has expired or is not yet valid'},
                status=status=HTTP_400_BAD_REQUEST
            )

        return Response({
            'success': True,
            'discount_percent': coupon.discount_percentage
        }, status=status.HTTP_200_OK)
