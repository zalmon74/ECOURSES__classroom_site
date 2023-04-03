from django.apps import AppConfig
from django.db.models import signals


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    
    verbose_name = 'Аккаунты'

    def ready(self) -> None:
        from .signals import create_default_all_groups
        signals.post_migrate.connect(create_default_all_groups, sender=self)

