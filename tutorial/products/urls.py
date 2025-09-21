from django.urls import path
from .views import ProductListCreateView, ProductDetailsView

urlpatterns = [
    # The URL will be products/
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),

    # This path is for a single product's detail, update, and delete.
    #Products/1/ where '1' is the product ID.
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='product-detail'),
]
