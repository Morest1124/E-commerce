from django.shortcuts import render 
from .models import Product
from rest_framework import generics
from serializers import ProductSerializer
# Create your views here.

# View for listing all products and creating a new product
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

# View for retrieving, updating, and deleting a single product
class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer