from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

# Create models here

class CustomUser(AbstractUser):
    """
    Custom user model with additional fields.
    """
    
    country_origin = models.CharField(max_length=50, blank=False, default='')
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    shipping_address = models.TextField(max_length=200, null=True, blank=True)
    identity_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    
    # These fields are required to avoid conflicts with Django's default user model
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
