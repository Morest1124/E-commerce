from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer

# Create your views here.
class UserProfileViews(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user_profile = request.user.profile
        except UserProfile.DoesNotExist:
            return Response({'message': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        try:
            user_profile = request.user.profile
        except UserProfile.DoesNotExist:
            return Response({'message': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs) # Simple patch implementation
