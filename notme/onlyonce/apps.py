from django.apps import AppConfig


class OnlyonceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'onlyonce'
