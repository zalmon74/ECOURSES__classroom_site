from accounts.models import CustomUser
from django import template
from django.conf import settings
from django.contrib.auth.models import Group
from training_course.models import Category, TrainingCourseModel

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
def show_nav_bar(user: CustomUser) -> dict:
    """Формирует список с данными для навигационной панели

    Args:
        user (CustomUser): Объект с текущим пользователем

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
         'url_name': 'contact_us', 
         'f_drop': False, 
         'lst_drop': []
        },
    ]
    nav_bar_subjects = []
    for categoty in Category.objects.all():
        nav_bar_subjects.append(
            {
                'name': categoty.name_visible,
                'url_name': 'index',
                'f_drop': False,
                'lst_drop': [],
            }
        )
    return {
        'nav_bar': nav_bar, 
        'nav_bar_subjects': nav_bar_subjects, 
        'user': user
    }


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
    lst_categories = []
    for category in Category.objects.all()[:8]:
        lst_categories.append(
            {
                'name': category.name_visible,
                'count_courses': category.trainingcoursemodel_set.count(),
                'url_name': 'index',
                'image': category.photo.url,
            }
        )
    return {'lst_categories': lst_categories}


@register.inclusion_tag('classroom/tags/show_index_courses.html')
def show_index_courses() -> dict:
    lst_courses = []
    for course in TrainingCourseModel.objects.all().order_by('?')[:6]:
        lst_courses.append(
            {
                'name': course.name,
                'count_students': course.max_count_students,
                'datetime_start': course.datetime_course_start,
                'datetime_end': course.datetime_course_end,
                'review': 0,
                'count_review': 0,
                'price': course.price,
                'url_name': 'index',
                'photo': course.photo.url,
            }
        )
    return {'lst_courses': lst_courses,}


@register.inclusion_tag('classroom/tags/show_index_our_teachers.html')
def show_index_our_teachers() -> dict:
    """ Формирует список с данными для "Лучших учителей" на главной  странице

    Returns:
        dict: Словарь, который содержит список с элементами для страницы
    """
    teachers = []
    for teacher in Group.objects.get(name=settings.NAME_DB_TEACHER_GROUP).user_set.all().order_by('?')[:4]:
        teachers.append(
            {'name': teacher.get_full_name(),
             'profession': teacher.moreinformationaboutteachers.profession,
             'photo': teacher.userphoto.photo.url,
             'href_vk': teacher.url_vk,
             'href_mail': teacher.url_email,
             'href_github': teacher.url_github,
            },
        )
    return {'teachers': teachers}


@register.inclusion_tag('classroom/tags/show_index_testimonial.html')
def show_index_testimonial() -> dict:
    """ Формирует список с данными для "Что говорят о нас ученики" на главной 
        странице

    Returns:
        dict: Словарь, который содержит список с элементами для страницы
    """
    reviews = [
        {'name': 'Эпископ Транов',
         'profession': 'Разработчик',
         'text': 'Dolor eirmod diam stet kasd sed. Aliqu rebum est eos. Rebum elitr dolore et eos labore, stet justo sed est sed. Diam sed sed dolor stet amet eirmod eos labore diam',
         'static_image': 'img/testimonial-1.jpg',
        },
        {'name': 'Джули Робин',
         'profession': 'HR-специалист',
         'text': 'Dolor eirmod diam stet kasd sed. Aliqu rebum est eos. Rebum elitr dolore et eos labore, stet justo sed est sed. Diam sed sed dolor stet amet eirmod eos labore diam',
         'static_image': 'img/testimonial-2.jpg',
        },
        {'name': 'Врундель Марнор',
         'profession': 'Маркетинг',
         'text': 'Dolor eirmod diam stet kasd sed. Aliqu rebum est eos. Rebum elitr dolore et eos labore, stet justo sed est sed. Diam sed sed dolor stet amet eirmod eos labore diam',
         'static_image': 'img/testimonial-3.jpg',
        },
    ]
    return {'reviews': reviews}


@register.inclusion_tag('classroom/tags/show_index_blog.html')
def show_index_blog() -> dict:
    """ Формирует список с данными для "Последние публикации" на главной 
        странице

    Returns:
        dict: Словарь, который содержит список с элементами для страницы
    """
    publications = [
        {'title': 'Lorem elitr magna stet eirmod labore amet labore clita at ut clita',
         'date': '19:09:2022',
         'static_image': 'img/blog-1.jpg',
        },
        {'title': 'Lorem elitr magna stet eirmod labore amet labore clita at ut clita',
         'date': '21:02:2021',
         'static_image': 'img/blog-2.jpg',
        },
        {'title': 'Lorem elitr magna stet eirmod labore amet labore clita at ut clita',
         'date': '01:12:2020',
         'static_image': 'img/blog-3.jpg',
        },
    ]
    return {'publications': publications}
