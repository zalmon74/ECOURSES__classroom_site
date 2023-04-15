import re

from django.core.validators import ValidationError


def validation_first_second_sur_name(name: str):
    """ Наличие только русских и латинских символов

    Args:
        name (str): Поле

    Raises:
        ValidationError: Вызывается, если поле содержит не только русские и 
            латинские символы
    """

    if not bool(re.search('[a-zA-Z]', name)) and not bool(re.search('[а-яА-Я]', name)):
        raise ValidationError(f'Поле может содержать только русские и латинские символы')


def validation_url_vk(url_vk: str):
    """ Правильный URL для профиля в ВК

    Args:
        url_vk (str): Введенный URL

    Raises:
        ValidationError: Вызывается, если введенный URL не соответствует 
            правильному
    """
    if not bool(re.search('vk.com/[a-zA-Z_.]{5,32}', url_vk)):
        raise ValidationError('Введите верный URL для профиля в ВК')


def validation_url_mail(url_mail: str):
    """ Правильный URL для почтового сервиса. Правильным считается, если в
        в URL имеется слово mail

    Args:
        url_mail (str): Введенный URL

    Raises:
        ValidationError: Вызывается, если введенный URL не соответствует 
            правильному
    """
    if not bool(re.search('mail', url_mail)):
        raise ValidationError('Введите верный URL для почтового сервиса')


def validation_url_github(url_github: str):
    """ Правильный URL для профиля github.

    Args:
        url_github (str): Введенный URL

    Raises:
        ValidationError: Вызывается, если введенный URL не соответствует 
            правильному
    """
    if not bool(re.search('github.com/[a-zA-Z_]{4,39}', url_github)):
        raise ValidationError('Введите верный URL для профиля на github')
