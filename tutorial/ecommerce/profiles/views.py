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
            User_Profile = request.user.profile
            
        except UserProfile.DoesNotExist:
            # If user profile does not exist return 404 not found error
            return Response({'message': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the profile data
        serializer = UserProfileSerializer(User_Profile)
            
        # Return a successful response with serialized data
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        # Try to get the user's profile to see if it already exists
        try:
            UserProfile.objects.get(user=request.user)
            # If the profile exists, return a 400 Bad Request
            return Response(
                {"message": "User profile already exists!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except UserProfile.DoesNotExist:
            # If the profile does not exist, we can proceed with creation
            pass

        # Instantiate the serializer with the incoming request data
        serializer = UserProfileSerializer(data=request.data)
        
        # Validate the data against the serializer's rules
        if serializer.is_valid():
            # If the data is valid, save the new profile
            serializer.save(user=request.user)
            
            # Return a successful response with the new data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # If the data is not valid, return the errors from the serializer
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)