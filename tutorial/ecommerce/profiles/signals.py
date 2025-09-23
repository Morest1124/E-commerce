from django.db.models.signals import post_save
from django.dispatch import receiver
from shopping.models import CustomUser
from .models import UserProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a user profile when a new user is created."""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    """Save the user profile when the user is saved."""
    instance.profile.save()
