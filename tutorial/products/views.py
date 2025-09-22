from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
# Create your views here.

# View for listing all products and creating a new product
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

# View for retrieving, updating, and deleting a single product
class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
# View for listing all categories and creating a new category
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# View for retrieving, updating, and deleting a single category
class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
