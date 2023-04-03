from django.db import models


def user_photo_upload_to(instance: models.Model, filename: str) -> str:
    """ Функция формирования пути сохранения фото

    Args:
        instance (models.Model): Объект фото, который необходимо сохранить
        filename (str): Имя файла

    Returns:
        str: Сформированный путь до файла
    """
    return 'user_photo/images/%s/%s' % (
        instance.user.get_full_name_with_email(), 
        filename
    )
