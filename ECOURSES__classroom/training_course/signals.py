import random
from datetime import datetime
from pathlib import Path
from shutil import copy
from typing import Any

from django.conf import settings
from django.contrib.auth.models import Group
from django.db.models import Model

from .help_functions import category_photo_upload_to, courses_photo_upload_to
from .models import (Category, MoreInformationAboutCourses, Tag,
                     TrainingCourseModel)


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


def create_default_trainingcourses(
    sender: TrainingCourseModel, 
    *args: list[Any], 
    **kwargs: dict[Any]
) -> None:
    """ Создание курсов по умолчанию, которые будут присутствовать на сайте
        после миграции

    Args:
        sender (Tag): Класс модели, которая добавляется в БД
    """
    # Путь до фото
    path_dir_with_photo = settings.PATH_DIR_DEFAULT_IMAGE_DB.joinpath('training_course')
    # Все пользователи, которые будут использоваться в курсах
    all_partners = Group.objects.get(name=settings.NAME_DB_PARTNER_GROUP).user_set.all()
    all_teachers = Group.objects.get(name=settings.NAME_DB_TEACHER_GROUP).user_set.all()
    all_students = Group.objects.get(name=settings.NAME_DB_STUDENT_GROUP).user_set.all()
    # Все категории
    all_categories = Category.objects.all()
    # Информация для создания курсов
    all_courses = [
        (
          'Веб дизайн для начинающих',  # name
          random.choice(all_partners),  # author
          all_categories.get(name='Digital Design'),  # category
          all_categories.get(name='Digital Design').tag_set.all(),  # tags
          2,  # max_count_teachers
          all_teachers.order_by('?')[:2],  # teachers
          10,  # max_count_students
          all_students.order_by('?')[:3],  # students
          'course1.jpg',  # photo
          12345,  # price
          datetime.fromisoformat('20230101'),  # datetime_course_start
          datetime.fromisoformat('20230301'),  # datetime_course_end,
          # MoreInformationAboutCourses
          """Веб-дизайнер проектирует сайты и приложения. Он такой же IT-специалист, как и программист. Именно он отвечает за внешний вид и удобство цифровых продуктов. Поэтому рынку нужны талантливые веб-дизайнеры, а работодатели готовы им хорошо платить.""",  # description
          """Знакомство с Figma.
             Основные инструменты Figma.
             Иконки, иллюстрации и картинки.
             Компоненты.
             Библиотеки компонентов и общие стили.
             Auto Layout и Variants.
             Сложные многостраничные документы.
             Дополнительные возможности и сообщество авторов.
             Подготовка макета для разработчиков.""",  # course_program
        ),
        (
          'Backend Python-разработчик',  # name
          random.choice(all_partners),  # author
          all_categories.get(name='Backend'),  # category
          all_categories.get(name='Backend').tag_set.all(),  # tags
          3,  # max_count_teachers
          all_teachers.order_by('?')[:2],  # teachers
          15,  # max_count_students
          all_students.order_by('?')[:1],  # students
          'course2.jpg',  # photo
          1234,  # price
          datetime.fromisoformat('20230201'),  # datetime_course_start
          datetime.fromisoformat('20230301'),  # datetime_course_end,
          # MoreInformationAboutCourses
          """Python — идеальный язык для новичка. Код на Python легко писать и читать, язык стабильно занимает высокие места в рейтингах популярности, а «питонисты» востребованы почти во всех сферах IT — программировании, анализе данных, системном администрировании и тестировании. YouTube, Intel, Pixar, NASA, VK, Яндекс — вот лишь немногие из известных компаний, которые используют Python в своих продуктах.""",  # description
          """Введение в веб-фреймворки.
             Введение в Django.
             Введение в веб и Linux.
             База данных и модели.
             Административный интерфейс в Django.
             Обработка запросов в Django.
             Формы.
             Class Based Views. Generic Views.
             Аутентификация и авторизация.
             Регистрация и права доступа..
             Тестирование.
             Работа с файлами.
             Локализация и интернационализация.
             Введение в Django REST Framework
             Документирование
             Эффективная работа с базой данных в django
             Логирование и профилирование
             Экспорт/импорт данных
             Оптимизация с помощью кэширования
             Деплой и командная разработка""",  # course_program
        ),
        (
          'Начинающий Frontend разработчик',  # name
          random.choice(all_partners),  # author
          all_categories.get(name='Frontend'),  # category
          all_categories.get(name='Frontend').tag_set.all(),  # tags
          3,  # max_count_teachers
          all_teachers.order_by('?')[:1],  # teachers
          15,  # max_count_students
          all_students.order_by('?')[:5],  # students
          'course3.jpg',  # photo
          1234,  # price
          datetime.fromisoformat('20230201'),  # datetime_course_start
          datetime.fromisoformat('20230301'),  # datetime_course_end,
          # MoreInformationAboutCourses
          """Бизнес активно переходит в онлайн, поэтому веб-сервисы нужны всем. Компании ищут frontend-разработчиков, чтобы внедрять фичи быстрее конкурентов. Работодатели ценят таких специалистов и предлагают гибкий график или постоянную удалёнку.""",  # description
          """Веб-вёрстка. Базовый уровень
             Javascript. Базовый уровень
             Фреймворк на выбор: React.js, Vue.js
             Node.js
             Typescript
             Карьерный курс: трудоустройство и развитие
             Трудоустройство с помощью Центра Карьеры""",  # course_program
        ),
        (
          'Профессия Data Scientist',  # name
          random.choice(all_partners),  # author
          all_categories.get(name='Data Science'),  # category
          all_categories.get(name='Data Science').tag_set.all(),  # tags
          1,  # max_count_teachers
          all_teachers.order_by('?')[:1],  # teachers
          7,  # max_count_students
          all_students.order_by('?')[:2],  # students
          'course4.jpg',  # photo
          123456,  # price
          datetime.fromisoformat('20230501'),  # datetime_course_start
          datetime.fromisoformat('20230701'),  # datetime_course_end,
          # MoreInformationAboutCourses
          """Освойте Data Science с нуля. Вы попробуете силы в аналитике данных, машинном обучении, дата-инженерии и подробно изучите направление, которое нравится вам больше. Отточите навыки на реальных проектах и станете востребованным специалистом.""",  # description
          """Введение в Data Science
             Machine Learning — машинное обучение
             Data Engineer — дата-инженер
             Data Analyst — дата-аналитик""",  # course_program
        ),
        (
          'Инженер по тестированию',  # name
          random.choice(all_partners),  # author
          all_categories.get(name='IT-Infrastructure'),  # category
          all_categories.get(name='IT-Infrastructure').tag_set.all(),  # tags
          1,  # max_count_teachers
          all_teachers.order_by('?')[:1],  # teachers
          7,  # max_count_students
          all_students.order_by('?')[:4],  # students
          'course5.jpg',  # photo
          23456,  # price
          datetime.fromisoformat('20230601'),  # datetime_course_start
          datetime.fromisoformat('20230901'),  # datetime_course_end,
          # MoreInformationAboutCourses
          """Вы научитесь находить ошибки в работе сайтов и приложений с помощью Java, JavaScript или Python. С первого занятия погрузитесь в практику и сможете начать зарабатывать уже через 4 месяца.""",  # description
          """Ручное тестирование веб-приложений
             Программа бета-тестирования от банка Открытие и ВКонтакте
             Ручное тестирование мобильных приложений
             Автоматизированное тестирование на JavaScript, Java или Python""",  # course_program
        ),
        (
          'Менеджер маркетплейсов',  # name
          random.choice(all_partners),  # author
          all_categories.get(name='Brand Marketing'),  # category
          all_categories.get(name='Brand Marketing').tag_set.all(),  # tags
          2,  # max_count_teachers
          all_teachers.order_by('?')[:2],  # teachers
          13,  # max_count_students
          all_students.order_by('?')[:4],  # students
          'course6.jpg',  # photo
          45213,  # price
          datetime.fromisoformat('20230801'),  # datetime_course_start
          datetime.fromisoformat('20231101'),  # datetime_course_end,
          # MoreInformationAboutCourses
          """Вы с нуля освоите востребованную и перспективную профессию. Узнаете, как сотрудничать с начинающими селлерами и крупными компаниями. Получите реальный бюджет на продвижение и сможете на старте зарабатывать от 60 000 рублей, не выходя из дома.""",  # description
          """Введение в работу с маркетплейсами. Основные понятия.
             Выбор товаров для торговли на маркетплейсах.
             Основы работы с самыми популярными маркетплейсами (Ozon, Wildberries, eBay, AliExpress и Яндекс.Маркет).
             Продвижение handmade-товаров на маркетплейсах («Ярмарка мастеров», Etsy, Amazon Handmade и другие).
             Как рассчитывать цены на маркетплейсах.
             Продвижение на маркетплейсах.
             Масштабируем магазин.
             Кейс. Подготовка стратегии продвижения на маркетплейсах.""",  # course_program
        ),
    ]
    # Создаем объекты и сохраняем их в БД
    for el in all_courses:
        obj = TrainingCourseModel(
            name=el[0],
            author=el[1],
            category=el[2],
            max_count_teachers=el[4],
            max_count_students=el[6],
            price=el[9],
            datetime_course_start=el[10],
            datetime_course_end=el[11],
        )        
        # Определяем путь до фото
        photo_media = courses_photo_upload_to(obj, el[8])
        obj.photo = photo_media
        # Создаем объект с дополнитльной информацией о курсе
        obj_more_info = MoreInformationAboutCourses(
            course=obj,
            description=el[12],
            course_program=el[13],
        )
        # Сохраняем объекты
        obj.save()
        obj_more_info.save()
        # Копируем фото в media
        path_media_image = Path(str(settings.MEDIA_ROOT) + '/' + photo_media)
        try:
            path_media_image.parent.mkdir(parents=True)
        except FileExistsError: # Если каталог уже создан
            pass
        path_image = str(path_dir_with_photo) + '/' + el[8]
        copy(path_image, path_media_image) 
        # Добавляем теги
        for tag in el[3]:
            obj.tags.add(tag)
        # Добавляем учителей
        for teacher in el[5]:
            obj.teachers.add(teacher)
        # Добавляем студентов
        for student in el[7]:
            obj.students.add(student)
