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


@register.inclusion_tag('classroom/tags/show_index_carousel.html')
def show_index_carousel() -> dict:
    """ Формирует список с данными для "карусели" на главной странице

    Returns:
        dict: Словарь, который содержит список с элементами
    """
    lst_carousel = [
        {'small_title': 'Лучшие онлайн курсы',
         'title': 'Лучшее образование из вашего дома',
         'text_button': 'Читать',
         'url_name': 'index',
         'static_image': 'img/carousel-1.jpg',
         'number': 0,
        },
        {'small_title': 'Лучшие онлайн курсы',
         'title': 'Лучшая платформа для онлайн-обучения',
         'text_button': 'Читать',
         'url_name': 'index',
         'static_image': 'img/carousel-2.jpg',
         'number': 1,
        },
        {'small_title': 'Лучшие онлайн курсы',
         'title': 'Новый способ учиться дома',
         'text_button': 'Читать',
         'url_name': 'index',
         'static_image': 'img/carousel-3.jpg',
         'number': 2,
        },
    ]
    return {
        'lst_carousel': lst_carousel, 
        'range_carousel': range(len(lst_carousel)),
    }


@register.inclusion_tag('classroom/tags/show_index_about.html')
def show_index_about() -> dict():
    """ Формирует список с данными для "о нас" на главной странице

    Returns:
        dict: Словарь, который содержит список с элементами для страницы
    """
    info = {
        'title': 'Инновационный способ обучения',
        'text': 'Aliquyam accusam clita nonumy ipsum sit sea clita ipsum clita, ipsum dolores amet voluptua duo dolores et sit ipsum rebum, sadipscing et erat eirmod diam kasd labore clita est. Diam sanctus gubergren sit rebum clita amet, sea est sea vero sed et. Sadipscing labore tempor at sit dolor clita consetetur diam. Diam ut diam tempor no et, lorem dolore invidunt no nonumy stet ea labore, dolor justo et sit gubergren diam sed sed no ipsum. Sit tempor ut nonumy elitr dolores justo aliquyam ipsum stet',
        'text_button': 'Читать',
        'url_name': 'index',
        'static_image': 'img/about.jpg',
    }
    return {'element': info}


@register.inclusion_tag('classroom/tags/show_index_categories.html')
def show_index_categories() -> dict():
    """ Формирует список с данными для "популярные направления" на главной 
        странице

    Returns:
        dict: Словарь, который содержит список с элементами для страницы
    """
    lst_categories = [
        {'name': 'Веб дизайн',
         'count_courses': 11,
         'url_name': 'index',
         'static_image': 'img/cat-1.jpg',
        },
        {'name': 'Разработка',
         'count_courses': 22,
         'url_name': 'index',
         'static_image': 'img/cat-2.jpg',
        },
        {'name': 'Дизайн игр',
         'count_courses': 33,
         'url_name': 'index',
         'static_image': 'img/cat-3.jpg',
        },
        {'name': 'Дизайн приложений',
         'count_courses': 44,
         'url_name': 'index',
         'static_image': 'img/cat-4.jpg',
        },
        {'name': 'Маркетинг',
         'count_courses': 55,
         'url_name': 'index',
         'static_image': 'img/cat-5.jpg',
        },
        {'name': 'Тестирование',
         'count_courses': 66,
         'url_name': 'index',
         'static_image': 'img/cat-6.jpg',
        },
        {'name': 'Автор контента',
         'count_courses': 77,
         'url_name': 'index',
         'static_image': 'img/cat-7.jpg',
        },
        {'name': 'SEO-продвижение',
         'count_courses': 88,
         'url_name': 'index',
         'static_image': 'img/cat-8.jpg',
        },
    ]
    return {'lst_categories': lst_categories}


@register.inclusion_tag('classroom/tags/show_index_courses.html')
def show_index_courses() -> dict:
    lst_courses = [
        {'name': 'Веб дизайн для начинающих',
         'count_students': 30,
         'datetime_start': "01.01.2023",
         'datetime_end': "01.05.2023",
         'review': 4.1,
         'count_review': 123,
         'price': 12345,
         'url_name': 'index',
         'static_image': 'img/course-1.jpg',
        },
        {'name': 'Веб дизайн для продвинутых',
         'count_students': 20,
         'datetime_start': "02.02.2023",
         'datetime_end': "02.06.2023",
         'review': 4.5,
         'count_review': 12,
         'price': 123456,
         'url_name': 'index',
         'static_image': 'img/course-2.jpg',
        },
        {'name': 'Веб дизайн для профессионалов',
         'count_students': 10,
         'datetime_start': "03.03.2023",
         'datetime_end': "03.08.2023",
         'review': 4.7,
         'count_review': 123,
         'price': 1234567,
         'url_name': 'index',
         'static_image': 'img/course-3.jpg',
        },
        {'name': 'Разработка для начинающих',
         'count_students': 30,
         'datetime_start': "01.01.2023",
         'datetime_end': "01.05.2023",
         'review': 4.1,
         'count_review': 123,
         'price': 12345,
         'url_name': 'index',
         'static_image': 'img/course-4.jpg',
        },
        {'name': 'Разработка для продвинутых',
         'count_students': 20,
         'datetime_start': "02.02.2023",
         'datetime_end': "02.06.2023",
         'review': 4.5,
         'count_review': 12,
         'price': 123456,
         'url_name': 'index',
         'static_image': 'img/course-5.jpg',
        },
        {'name': 'Разработка для профессионалов',
         'count_students': 10,
         'datetime_start': "03.03.2023",
         'datetime_end': "03.08.2023",
         'review': 4.7,
         'count_review': 123,
         'price': 1234567,
         'url_name': 'index',
         'static_image': 'img/course-6.jpg',
        },
    ]
    return {'lst_courses': lst_courses,}
