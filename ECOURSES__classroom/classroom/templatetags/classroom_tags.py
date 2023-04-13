from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('classroom/tags/show_top_bar.html')
def show_top_bar() -> dict:
    """ Формирует список с данными для топ-панели

    Returns:
        list: Список, который хранит данные для top-панели
    """
    top_bar = [
        {'name': 'Офис', 
         'text': settings.TEXT_ADRESS_ABOUT_CITY, 
         'classimage': 'fa-map-marker-alt'
        },
        {'name': 'Email', 
         'text': settings.TEXT_ABOUT_EMAIL, 
         'classimage': 'fa-envelope'
        },
        {'name': 'Связаться', 
         'text': settings.TEXT_ABOUT_NUMBER_PHONE, 
         'classimage': 'fa-phone'
        },
    ]
    return {'top_bar': top_bar}


@register.inclusion_tag('classroom/tags/nav_bar/show_nav_bar.html')
def show_nav_bar() -> dict:
    """ Формирует список с данными для навигационной панели

    Returns:
        dict: Словарь, который хранит список с данными для навигационной панели
    """
    nav_bar = [
        {'name': 'Домашняя', 
         'url_name': 'index', 
         'f_drop': False, 
         'lst_drop': []
        },
        {'name': 'О нас', 
         'url_name': 'index', 
         'f_drop': False, 
         'lst_drop': []
        },
        {'name': 'Курсы', 
         'url_name': 'index', 
         'f_drop': False, 
         'lst_drop': []
        },
        {'name': 'Учителя', 
         'url_name': 'index', 
         'f_drop': False, 
         'lst_drop': []
        },
        {'name': 'Блог', 
         'url_name': 'index', 
         'f_drop': True, 
         'lst_drop': [
             {'name': 'Все посты', 
              'url_name': 'index', 
              'f_drop': False, 
              'lst_drop': []
             },
             {'name': 'Пост', 
              'url_name': 'index', 
              'f_drop': False, 
              'lst_drop': []
             },
         ]
        },
        {'name': 'Связаться', 
         'url_name': 'index', 
         'f_drop': False, 
         'lst_drop': []
        },
    ]
    nav_bar_subjects = [
        {'name': 'Веб дизайн', 
         'url_name': 'index', 
         'f_drop': True, 
         'lst_drop': [
            {'name': 'HTML', 
             'url_name': 'index', 
             'f_drop': False, 
             'lst_drop': []
            },
            {'name': 'CSS', 
             'url_name': 'index', 
             'f_drop': False, 
             'lst_drop': []
            },
            {'name': 'jQuery', 
             'url_name': 'index', 
             'f_drop': False, 
             'lst_drop': []
            },
         ]
        },
        {'name': 'Дизайн приложений', 
         'url_name': 'index', 
         'f_drop': False, 
         'lst_drop': []
        },
        {'name': 'Тестирование', 
         'url_name': 'index', 
         'f_drop': False, 
         'lst_drop': []
        },
        {'name': 'SEO', 
         'url_name': 'index', 
         'f_drop': False, 
         'lst_drop': []
        },
    ]
    return {'nav_bar': nav_bar, 'nav_bar_subjects': nav_bar_subjects,}


@register.inclusion_tag('classroom/tags/nav_bar/show_nav_bar_element.html')
def show_nav_bar_element(element: dict) -> dict:
    """ Отображает в навигационном меню элемент

    Args:
        element (dict): Словарь типа:
        {'name': 'data', 'url_name: 'data', 'f_drop': 'data', lst_drop: [data]},
        где name - Имя элемента, которое будет отобржаться в списке;
            url_name - Имя url страницы
            f_drop - Флаг, что данный элемент имеет выпадающий список
            lst_drop - список, который содержит элементы, которые будут в 
                выпадающем списке

    Returns:
        dict: Содержит элемент, который необходимо отобразить
    """
    return {'element': element}


@register.inclusion_tag('classroom/tags/nav_bar/show_nav_bar_subjects_element.html')
def show_nav_bar_subjects_element(element: dict) -> dict:
    """ Отображает в навигационном меню элемент c направления обучения

    Args:
        element (dict): Словарь типа:
        {'name': 'data', 'url_name: 'data', 'f_drop': 'data', lst_drop: [data]},
        где name - Имя элемента, которое будет отобржаться в списке;
            url_name - Имя url страницы
            f_drop - Флаг, что данный элемент имеет выпадающий список
            lst_drop - список, который содержит элементы, которые будут в 
                выпадающем списке

    Returns:
        dict: Содержит элемент, который необходимо отобразить
    """
    return {'element': element}


@register.inclusion_tag('classroom/tags/footer/show_footer.html')
def show_footer() -> dict:
    lst_coureses = [
        {'name': 'Веб дизайн', 'url_name': 'index'},
        {'name': 'Дизайн приложений', 'url_name': 'index'},
        {'name': 'Маркетинг', 'url_name': 'index'},
        {'name': 'Тестирование', 'url_name': 'index'},
        {'name': 'SEO', 'url_name': 'index'},
    ]
    return {'lst_coureses': lst_coureses}


@register.inclusion_tag('classroom/tags/footer/show_footer_get_in_touch.html')
def show_footer_get_in_touch() -> dict:
    """ Формирует список с данными для "связаться с нами" в футуре

    Returns:
        dict: Словарь, который содержит список с элементами
    """
    lst_get_in_touch = [
        {'name': 'Офис', 
         'text': settings.TEXT_ADRESS_ABOUT_CITY, 
         'classimage': 'fa-map-marker-alt'
        },
        {'name': 'Email', 
         'text': settings.TEXT_ABOUT_EMAIL, 
         'classimage': 'fa-envelope'
        },
        {'name': 'Связаться', 
         'text': settings.TEXT_ABOUT_NUMBER_PHONE, 
         'classimage': 'fa-phone-alt'
        },
    ]
    lst_links_get_in_touch = [
        {'class': 'fa-github', 'url_name': settings.URL_GITHUB_AUTHOR},
        {'class': 'fa-vk', 'url_name': settings.URL_VK_AUTHOR},
    ]    
    return {
        'lst_get_in_touch': lst_get_in_touch, 
        'lst_links_get_in_touch': lst_links_get_in_touch
    }
