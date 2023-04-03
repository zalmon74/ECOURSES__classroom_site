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
