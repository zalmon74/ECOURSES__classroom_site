from django import template

register = template.Library()


@register.inclusion_tag('classroom/tags/show_top_bar.html')
def show_top_bar() -> dict:
    """ Формирует список с данными для топ-панели

    Returns:
        list: Список, который хранит данные для top-панели
    """
    top_bar = [
        {'name': 'Офис', 
         'text': 'Улица 123, Красноярск, РФ', 
         'classimage': 'fa-map-marker-alt'
        },
        {'name': 'Email', 
         'text': 'zalmon74@yandex.ru', 
         'classimage': 'fa-envelope'
        },
        {'name': 'Связаться', 
         'text': '+7(123) 456-78-90', 
         'classimage': 'fa-phone'
        },
    ]
    return {'top_bar': top_bar}
