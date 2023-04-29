from django.apps import AppConfig
from django.db.models import signals


class TrainingCourseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'training_course'

    verbose_name = 'Учебные курсы'

    def ready(self) -> None:
        from .signals import create_default_categories, create_default_tags
        signals.post_migrate.connect(create_default_categories, sender=self)
        signals.post_migrate.connect(create_default_tags, sender=self)
