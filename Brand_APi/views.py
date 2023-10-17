# Brand_Api/views.py

#from rest_framework import viewsets
from .models import Brand
from .serializers import BrandSerializer

#class BrandViewSet(viewsets.ModelViewSet):
 #   queryset = Brand.objects.all()
  #  serializer_class = BrandSerializer

from django.shortcuts import render
from Brand_APi . models import APi

def brand_api(request):
    brand = Brand.objects.all() # complex data 


    
