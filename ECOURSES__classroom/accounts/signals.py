from typing import Any

from django.conf import settings
from django.contrib.auth.models import Group
from django.db.models.base import ModelBase

from .models import CustomUser


def create_default_all_groups(
    sender: ModelBase, 
    *args: list[Any], 
    **kwargs: dict[Any]
) -> None:
    """ Создание стандартных групп пользователей

    Args:
        sender (ModelBase): Класс, который добавляется в БД
    """
    list_group = [Group(name=_) for _ in settings.ALL_GROUPS.keys()]
    Group.objects.bulk_create(list_group)
    
    
def user_registration(
    sender: ModelBase, 
    instance: CustomUser, 
    created: bool, 
    **kwargs: dict[Any]
) -> None:
    """ Добавление пользователя в БД.

    Args:
        sender (ModelBase): Класс, который добавляется в БД
        instance (CustomUser): Объект, который сохраняется в БД
        created (bool): флаг создания модели
    """
    if created and hasattr(instance, 'role'):
        group = Group.objects.get(name=instance.role)
        instance.groups.add(group)
    
    # Добавляем пользователя в группу администраторов, если он имеет статус
    # администратора
    if instance.is_staff:
        instance.groups.clear()
        group = Group.objects.get(name=settings.NAME_DB_ADMIN_GROUP)
        instance.groups.add(group)
        


