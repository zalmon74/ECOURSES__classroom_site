import random
from pathlib import Path
from shutil import copy
from typing import Any

from django.conf import settings
from django.contrib.auth.models import Group
from django.db.models import Model

from .help_functions import category_photo_upload_to
from .models import Category, Tag, TrainingCourseModel


def create_default_categories(
    sender: Category, 
    *args: list[Any], 
    **kwargs: dict[Any]
) -> None:
    """ Создание стандартных категорий, которые будут присутствовать на сайте
        после миграции

    Args:
        sender (Category): Класс модели, которая добавляется в БД
    """
    # Формируем путь для фото с категориями
    path_dir_image_categories = settings.PATH_DIR_DEFAULT_IMAGE_DB.joinpath('categories')
    # Список с именами категорий и их фото, которые будут добавляется в БД
    categories = [
        # Программирование
        ('Backend', 'Бэкенд-разработка', 'backend.jpg'),
        ('Frontend', 'Фронтенд-разработка', 'frontend.png'),
        ('Mobile', 'Мобильная разработка', 'mobile.png'),
        ('Data Science', 'Анализ данных', 'data_science.jpg'),
        ('IT-Infrastructure', 'IT-инфраструктура', 'it.jpg'),
        # Дизайн
        ('Digital Design', 'Цифровой дизайн', 'd_design.jpg'),
        ('Environment Design', 'Дизайн среды', 'e_design.jpg'),
        # Маркетинг
        ('Brand Marketing', 'Бренд-маркетинг', 'b_marketing.jpg'),
        ('Analytics', 'Аналитика', 'analytics.jpg'),
    ]
    for el in categories:
        # Создаем объект для сохранения в БД и сохраняем его
        obj = Category(name=el[0], name_visible=el[1])        
        photo_media = category_photo_upload_to(obj, el[2])
        obj.photo = photo_media
        obj.save()
        # Коприуем картинку в media
        path_media_image = Path(str(settings.MEDIA_ROOT) + '/' + photo_media)
        try:
            path_media_image.parent.mkdir(parents=True)
        except FileExistsError: # Если каталог уже создан
            pass
        path_image = str(path_dir_image_categories) + '/' + el[2]
        copy(path_image, path_media_image) 
    

def create_default_tags(
    sender: Tag, 
    *args: list[Any], 
    **kwargs: dict[Any]
) -> None:
    """ Создание стандартных тегов, которые будут присутствовать на сайте
        после миграции

    Args:
        sender (Tag): Класс модели, которая добавляется в БД
    """
    # Все категории
    all_categories = Category.objects.all()
    categories_development = all_categories.filter(name__in=('Backend', 'Frontend', 'Mobile', 'Data Science', 'IT-Infrastructure'))
    categories_design = all_categories.filter(name__in=('Digital Design', 'Environment Design'))
    categories_marketing = all_categories.filter(name__in=('Brand Marketing', 'Analytics'))
    # Теги
    tags = [
        # Общие теги
        (
            'Development',
            'Разработка', 
            categories_development,
        ),
        (
            'Programming', 
            'Программирование',
            categories_development,
        ),
        (
            'Design', 
            'Дизайн',
            categories_design,
        ),
        (
            'Marketing', 
            'Макретинг',
            categories_marketing
        ),
        (
            'New Profession', 
            'Новая профессия',
            all_categories
        ),
        (
            'Website layout', 
            'Верстка сайта',
            all_categories.filter(name__in=('Frontend', 'Digital Design'))
        ),
        (
            'Data Scientist', 
            'Специалист по данным',
            all_categories.filter(name=('Data Science', 'IT-Infrastructure', 'Analytics',))
        ),
        (
            'Network engineering', 
            'Cетевая инженерия',
            all_categories.filter(name=('Backend', 'IT-Infrastructure',))
        ),
        (
            'QA', 
            'Тестирование',
            categories_development,
        ),
        (
            'Web-Design', 
            'Веб-Дизайн',
            all_categories.filter(name__in=('Frontend', 'Digital Design'))
        ),
        (
            'Information Technology', 
            'Информационные технологии',
            categories_development
        ),
        (
            'Database', 
            'Базы данных',
            categories_development,
        ),
        # Программирование
        (
            'Backend', 
            'Бэкенд',
            all_categories.filter(name__in=('Backend', 'Mobile', 'IT-Infrastructure')),
        ),
        (
            'Frontend', 
            'Фронтенд',
            all_categories.filter(name__in=('Frontend', 'Mobile', 'IT-Infrastructure')),
        ),
        (
            'Web-development', 
            'Веб-разработка',
            categories_development.exclude(name='Data Science')
        ),
        (
            'fullstack', 
            'fullstack',
            categories_development.exclude(name='Data Science')
        ),
        (
            'devops', 
            'devops',
            (all_categories.get(name='IT-Infrastructure'),)
        ),
        (
            'OOP', 
            'ООП',
            categories_development,
        ),
        (
            'Mobile development', 
            'Мобильная разработка',
            categories_development.exclude(name='Data Science'),
        ),
        (
            'Android', 
            'Андроид',
            categories_development.exclude(name='Data Science'),
        ),
        (
            'ios', 
            'ios',
            categories_development.exclude(name='Data Science'),
        ),
        (
            'git', 
            'git',
            categories_development,
        ),
        # Языки программирование
        (
            'python', 
            'python',
            all_categories.filter(name=('Backend', 'Data Science', 'IT-Infrastructure',))
        ),
        (
            'python3', 
            'python3',
            all_categories.filter(name=('Backend', 'Data Science', 'IT-Infrastructure',))
        ),
        (
            'С', 
            'С',
            categories_development,
        ),
        (
            'С++', 
            'С++',
            categories_development,
        ),
        (
            'С#', 
            'С#',
            categories_development,
        ),
        (
            'JS', 
            'JS',
            categories_development,
        ),
        (
            'java script', 
            'java script',
            categories_development,
        ),
        (
            'typescript', 
            'typescript',
            categories_development,
        ),
        (
            'SQL', 
            'SQL',
            categories_development,
        ),
        (
            'Kotlin', 
            'Kotlin',
            categories_development,
        ),
        (
            'Java', 
            'Java',
            categories_development,
        ),
        # Фреймворки
        (
            'Reactjs', 
            'reactjs',
            categories_development.exclude(name='Backend'),
        ),
        (
            'Django', 
            'Django',
            categories_development.exclude(name='Frontend'),
        ),
        (
            '.net', 
            '.net',
            categories_development.exclude(name='Frontend'),
        ),
        # Языки описания
        (
            'CSS', 
            'CSS',
            all_categories.filter(name__in=('Frontend', 'Digital Design')),
        ),
        (
            'CSS3', 
            'CSS3',
            all_categories.filter(name__in=('Frontend', 'Digital Design')),
        ),
        (
            'html', 
            'html',
            all_categories.filter(name__in=('Frontend', 'Digital Design')),
        ),
        (
            'html5', 
            'html5',
            all_categories.filter(name__in=('Frontend', 'Digital Design')),
        ),
        # Дизайн
        (
            'UI', 
            'UI',
            categories_design,
        ),
        (
            'UI-Design', 
            'UI-Дизайн',
            categories_design,
        ),
        (
            'UX', 
            'UX',
            categories_design,
        ),
        (
            'UX-Design', 
            'UX-Дизайн',
            categories_design,
        ),
    ]
    for el in tags:
        tag = Tag(name=el[0], name_visible=el[1])
        tag.save()
        for category in el[2]:
            tag.categories.add(category)


