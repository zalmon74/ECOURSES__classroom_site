from django import template
from django.forms import Form

register = template.Library()


@register.inclusion_tag('accounts/tags/show_form.html')
def show_form(form: Form, title: str, text_button: str) -> dict:
    """ Тэг формирует отображение формы

    Args:
        form (Form): Форма, которую необходимо отобразить
        title (str): Заголовок над формой
        text_button (str): текст на кнопке после формы

    Returns:
        dict: Словарь, который объеденяет все объекты вместе для html-шаблона
    """
    return {'form': form, 'title': title, 'text_button': text_button}
