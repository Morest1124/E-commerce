from django.db import models
from shopping.models import CustomUser
from products.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.CharField(unique=True)
    status = models.CharField('pending')
    total_price = models.DecimalField(max_digits=10)
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
        
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL )
    quantity = models.IntegerField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f"Order item for {self.product.name} in order {self.order.id}"