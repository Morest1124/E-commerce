from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        models = UserProfile
        fields = 'user', 'address', 'phone_number'
        
        