from rest_framework import serializers
from models import Product, Category

#serializers
class ProductSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(max_length = 100)
    slug = serializers.SlugField(max_length = 2000)
    
class CategorySerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(Required= True, allow_blank = False, max_length = 100)
    description = serializers.CharField(Required= True, allow_blank = False, max_length = 2000)
    price = serializers.DecimalField(Required= True, allow_blank = False, max_digits= 10, decimal_places=2)
    stock = serializers.IntegerField(Required= True, allow_blank = False, max_length = 10)
    
    class Meta:
        models = Product, Category
        fields = 'id', 'name','slug' , 'name' ,'description','stock'
        read_only_fields = 'id'