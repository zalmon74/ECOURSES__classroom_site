from django.conf import settings
from django.contrib.auth.models import Group


def create_default_all_groups(sender, *args, **kwargs):
    """ Создание стандартных групп пользователей
    """
    list_group = [Group(name=_) for _ in settings.ALL_GROUPS.values()]
    Group.objects.bulk_create(list_group)
    

