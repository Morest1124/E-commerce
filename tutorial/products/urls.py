from django.urls import path
from .views import ProductListCreateView, ProductDetailsView, CategoryDetailsView, CategoryListCreateView



urlpatterns = [
    # URL will be /api/products/
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    # URL will be /api/products/1/
    path('<int:pk>/', ProductDetailsView.as_view(), name='product-detail'),
    # Category URLs remain the same but under /api/products/
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailsView.as_view(), name='category-detail'),
]