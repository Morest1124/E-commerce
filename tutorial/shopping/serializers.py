from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

def get_name_from_identity(identity_number):
    """
    Placeholder function to get name and surname from identity number.
    Replace this with your actual implementation.
    """
    # In a real implementation, you would make an API call to an external service.
    # For now, we'll just return some dummy data.
    print(f"Fetching name for identity number: {identity_number}")
    return "John", "Doe"

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    identity_number = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'country_origin', 'phone_number', 'shipping_address', 'identity_number')

    def create(self, validated_data):
        identity_number = validated_data['identity_number']
        first_name, last_name = get_name_from_identity(identity_number)

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=first_name,
            last_name=last_name,
            country_origin=validated_data.get('country_origin', ''),
            phone_number=validated_data.get('phone_number', None),
            shipping_address=validated_data.get('shipping_address', ''),
            identity_number=make_password(identity_number)
        )
        return user

