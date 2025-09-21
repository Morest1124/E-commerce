from rest_framework import serializers
from models import CustomUser

#serializers

class UserSerializers(serializers.ModelSerializer):
    emial = serializers.CharField(Required= True, allow_blank = False, max_length = 100)
    phone_number = serializers.IntegerField(Required = True, allow_blank = False)
    Shipping_address = serializers.CharField(Required = True, allow_blank = False, max_length = 200)
    
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'shipping_address', 'identity_number')
        read_only_fields = ('id')
        extra_kwargs = {'password': {'write_only': True}}


