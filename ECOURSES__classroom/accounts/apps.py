from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.models import signals


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    
    verbose_name = 'Аккаунты'

    def ready(self) -> None:
        from .signals import create_default_all_groups, user_registration
        signals.post_migrate.connect(create_default_all_groups, sender=self)
        signals.post_save.connect(user_registration, sender=get_user_model())
