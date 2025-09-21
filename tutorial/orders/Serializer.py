from rest_framework import serializers
from .models import Order, OrderItem

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        filds = '__all__'
        
class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        filds = '__all__'