from pathlib import Path
from shutil import copy
from typing import Any

from django.conf import settings
from django.contrib.auth.models import Group
from django.db.models.base import ModelBase

from .help_functions import user_photo_upload_to
from .models import CustomUser, UserPhoto


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


def create_default_superuser(
    sender: ModelBase, 
    *args: list[Any],
    **kwargs: dict[Any]
) -> None:
    """ Создает стандартных Суперадминистраторов

    Args:
        sender (ModelBase): Класс, который добавляется в БД
    """
    all_superuser = [
        (
            'admin@admin.ru',  # email
            'admin', # password
            'Супер',  # first_name
            'Администратор',  # second_name
        ),
    ]
    for el in all_superuser:
        CustomUser.objects.create_superuser(el[0], el[1], el[2], el[3])


def create_obj_customuser_with_photo_and_save_db(
    data: tuple, 
    path_dir_with_photo: Path
) -> None:
    """ Функция создает объект с пользователем, а также объект с фото для его 
        профиля, после чего записывает объект в БД

    Args:
        data (tuple): кортеж, который содержит следующие элементы:
            [0] - роль, под которой необходимо создать аккаунт (role)
            [1] - имя пользователя (first_name)
            [2] - пароль (password)
            [3] - фамилия пользователя (second_name)
            [4] - имя файла 
        path_dir_with_photo (Path): объект, который описывает путь до каталога
            с фото, которые будут записываться в БД
    """
    # Создаем объект, для сохранения данных в БД
    obj = CustomUser(
        email=data[1],
        first_name=data[3],
        second_name=data[4],
    )
    obj.set_password(data[2])
    obj.role = data[0]
    # Создаем объект с фото
    obj_photo = UserPhoto(user=obj)
    # Опеределяем путь для фото
    photo_media = user_photo_upload_to(obj_photo, data[5])
    obj_photo.photo = photo_media
    # Сохраняем объекты
    obj.save()
    obj_photo.save()
    # Копируем фото в media
    path_media_image = Path(str(settings.MEDIA_ROOT) + '/' + photo_media)
    try:
        path_media_image.parent.mkdir(parents=True)
    except FileExistsError: # Если каталог уже создан
        pass
    path_image = str(path_dir_with_photo) + '/' + data[5]
    copy(path_image, path_media_image) 


def create_defaults_administrators(
    sender: ModelBase, 
    *args: list[Any],
    **kwargs: dict[Any]
) -> None:
    """ Создание по умолчанию администраторов

    Args:
        sender (ModelBase): Класс, который добавляется в БД
    """
    # Формируем путь для фото для профиля
    path_dir_image_administrators = settings.PATH_DIR_DEFAULT_IMAGE_DB.joinpath('accounts').joinpath('administrators')
    # Список, который хранит данные для создания объектов
    all_administrators = [
        (
            settings.NAME_DB_ADMIN_GROUP,  # role
            'user1@administrator.ru',  # email
            'user1',  # password
            'Первый',  # first_name
            'Администратор',  # second_name
            'administrator1.png',  # name_file_for_photo
        ),
        (
            settings.NAME_DB_ADMIN_GROUP,  # role
            'user2@administrator.ru',  # email
            'user2',  # password
            'Второй',  # first_name
            'Администратор',  # second_name
            'administrator2.png',  # name_file_for_photo
        ),
        (
            settings.NAME_DB_ADMIN_GROUP,  # role
            'user3@administrator.ru',  # email
            'user3',  # password
            'Третий',  # first_name
            'Администратор',  # second_name
            'administrator3.png',  # name_file_for_photo
        ),
        (
            settings.NAME_DB_ADMIN_GROUP,  # role
            'user4@administrator.ru',  # email
            'user4',  # password
            'Четвертый',  # first_name
            'Администратор',  # second_name
            'administrator4.png',  # name_file_for_photo
        ),
        (
            settings.NAME_DB_ADMIN_GROUP,  # role
            'user5@administrator.ru',  # email
            'user5',  # password
            'Пятый',  # first_name
            'Администратор',  # second_name
            'administrator5.png',  # name_file_for_photo
        ),
    ]
    
    for el in all_administrators:
        create_obj_customuser_with_photo_and_save_db(el, path_dir_image_administrators)        
        

def create_defaults_partners(
    sender: ModelBase, 
    *args: list[Any],
    **kwargs: dict[Any]
) -> None:
    """ Создание по умолчанию партнеров

    Args:
        sender (ModelBase): Класс, который добавляется в БД
    """
    # Формируем путь для фото для профиля
    path_dir_image_partners = settings.PATH_DIR_DEFAULT_IMAGE_DB.joinpath('accounts').joinpath('partners')
    # Список, который хранит данные для создания объектов
    all_partners = [
        (
            settings.NAME_DB_PARTNER_GROUP,  # role
            'user1@partner.ru',  # email
            'user1',  # password
            'Первый',  # first_name
            'Партнер',  # second_name
            'partner1.png',  # name_file_for_photo
        ),
        (
            settings.NAME_DB_PARTNER_GROUP,  # role
            'user2@partner.ru',  # email
            'user1',  # password
            'Второй',  # first_name
            'Партнер',  # second_name
            'partner2.png',  # name_file_for_photo
        ),
        (
            settings.NAME_DB_PARTNER_GROUP,  # role
            'user3@partner.ru',  # email
            'user3',  # password
            'Третий',  # first_name
            'Партнер',  # second_name
            'partner3.png',  # name_file_for_photo
        ),
        (
            settings.NAME_DB_PARTNER_GROUP,  # role
            'user4@partner.ru',  # email
            'user4',  # password
            'Четвертый',  # first_name
            'Партнер',  # second_name
            'partner4.png',  # name_file_for_photo
        ),
        (
            settings.NAME_DB_PARTNER_GROUP,  # role
            'user5@partner.ru',  # email
            'user5',  # password
            'Пятый',  # first_name
            'Партнер',  # second_name
            'partner5.png',  # name_file_for_photo
        ),
    ]
    
    for el in all_partners:
        create_obj_customuser_with_photo_and_save_db(el, path_dir_image_partners)   
