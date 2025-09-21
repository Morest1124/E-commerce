from .views import UserProfileViews
from django.urls import path

urlpatterns = [
    path('profile/', UserProfileViews.as_view(), name='user-profile'),
]
