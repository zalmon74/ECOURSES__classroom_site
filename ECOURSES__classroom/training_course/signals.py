from pathlib import Path
from shutil import copy
from typing import Any

from django.conf import settings
from django.db.models import Model

from .help_functions import category_photo_upload_to
from .models import Category, Tag


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
    tags = [
        # Общие теги
        ('Development', 'Разработка'),
        ('Programming', 'Программирование'),
        ('Design', 'Дизайн'),
        ('Marketing', 'Макретинг'),
        ('New Profession', 'Новая профессия'),
        ('Website layout', 'Верстка сайта'),
        ('Data Scientist', 'Специалист по данным'),
        ('Network engineering', 'Cетевая инженерия'),
        ('QA', 'Тестирование'),
        ('Web-Design', 'Веб-Дизайн'),
        ('Information Technology', 'Информационные технологии'),
        ('Database', 'Базы данных'),
        # Программирование
        ('Backend', 'Бэкенд'),
        ('Frontend', 'Фронтенд'),
        ('Web-development', 'Веб-разработка'),
        ('fullstack', 'fullstack'),
        ('devops', 'devops'),
        ('OOP', 'ООП'),
        ('Mobile development', 'Мобильная разработка'),
        ('Android', 'Андроид'),
        ('ios', 'ios'),
        ('git', 'git'),
        # Языки программирование
        ('python', 'python'),
        ('python3', 'python3'),
        ('С', 'С'),
        ('С++', 'С++'),
        ('С#', 'С#'),
        ('JS', 'JS'),
        ('java script', 'java script'),
        ('typescript', 'typescript'),
        ('SQL', 'SQL'),
        ('Kotlin', 'Kotlin'),
        ('Java', 'Java'),
        # Фреймворки
        ('Reactjs', 'reactjs'),
        ('Django', 'Django'),
        ('.net', '.net'),
        # Языки описания
        ('CSS', 'CSS'),
        ('CSS3', 'CSS3'),
        ('html', 'html'),
        ('html5', 'html5'),
        # Дизайн
        ('UI', 'UI'),
        ('UI-Design', 'UI-Дизайн'),
        ('UX', 'UX'),
        ('UX-Design', 'UX-Дизайн'),
    ]
    all_obj_tags = []
    for el in tags:
        tag = Tag(name=el[0], name_visible=el[1])
        all_obj_tags.append(tag)
    Tag.objects.bulk_create(all_obj_tags)
