from django.apps import AppConfig

class HacknicheConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Hackniche'

    def ready(self):
        import Hackniche.signals
