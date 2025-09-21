from django.db import models
from shopping.models import CustomUser
from products.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
        
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        product_name = self.product.name if self.product else "Deleted Product"
        return f"Order item for {product_name} in order {self.order.id}"