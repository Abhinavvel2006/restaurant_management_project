from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializer import MenuCategorySerializer

class MenuCategoryListView(ListAPIView):
    queryset=MenuCategory.objects.all()
    serializer_class=MenuCategorySerializer

