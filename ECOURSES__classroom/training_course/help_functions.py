from django.db.models import Model


def category_photo_upload_to(instance: Model, filename: str) -> str:
    """ Функция формирования пути сохранения фото для категорий

    Args:
        instance (Model): Объект модели
        filename (str): Имя файла

    Returns:
        str: Сформированный путь до файла
    """
    return 'categories/images/%s/%s' % (instance.name, filename)


def courses_photo_upload_to(instance: Model, filename: str) -> str:
    """ Функция формирования пути сохранения фото для кусров

    Args:
        instance (Model): Объект модели
        filename (str): Имя файла

    Returns:
        str: Сформированный путь до файла
    """
    return 'courses/images/%s/%s/%s' % (instance.category, instance.name, filename)
