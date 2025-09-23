from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce.profiles'

    def ready(self):
        import ecommerce.profiles.signals
