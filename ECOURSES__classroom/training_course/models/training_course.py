from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CheckConstraint, F, Q

from .category import Category
from .tag import Tag


class TrainingCourseModel(models.Model):
    """ Описывает курс на сайте
    """
    name = models.CharField(
        max_length=100,
        verbose_name='Название курса'
    )
    author = models.ForeignKey(
        get_user_model(),
        related_name='trainingcourse_author',
        on_delete=models.PROTECT,
        verbose_name='Автор курса',
        help_text='Пользователь, который создал курс'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='Категория курса'
    )
    tags = models.ManyToManyField(Tag, verbose_name='Теги курса')
    max_count_teachers = models.PositiveSmallIntegerField(
        verbose_name='Максимальное количество учителей на курсе'
    )
    teachers = models.ManyToManyField(
        get_user_model(),
        related_name='trainingcourse_teachers',
        verbose_name='Учителя на курсе'
    )
    max_count_students = models.PositiveSmallIntegerField(
        verbose_name='Максимальное количество студентов на курсе'
    )
    students = models.ManyToManyField(
        get_user_model(),
        related_name='trainingcourse_students',
        verbose_name='Студенты на курсе'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена за курс'
    )
    f_stop = models.BooleanField(
        verbose_name='Флаг окончания курса',
        default=False
    )
    datetime_course_start = models.DateTimeField(
        verbose_name='Дата начала курса',
    )
    datetime_course_end = models.DateTimeField(
        verbose_name='Дата окончания курса',
    )
    created = models.DateTimeField(
        verbose_name='Дата создания курса',
        auto_now_add=True
    )
    
    class Meta:
        
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        
        constraints = [
            # max_count_teachers > 0
            CheckConstraint(
                check=Q(max_count_teachers__gt=0),
                name='check_max_count_teachers_gt_null',
                violation_error_message='Максимальное количество учителей на курсе не может быть равное 0',
            ),
            # max_count_students > 0
            CheckConstraint(
                check=Q(max_count_students__gt=0),
                name='check_max_count_students_gt_null',
                violation_error_message='Максимальное количество студентов на курсе не может быть равное 0',
            ),
            # datetime_course_end > datetime_course_start
            CheckConstraint(
                check=Q(datetime_course_end__gt=F('datetime_course_start')),
                name='check_datetime_course_end__gt__datetime_course_start',
                violation_error_message='Дата окончания курса не может превышать дату начала курса',
            )            
        ]

    def __str__(self) -> str:
        return f'{self.name} - {self.author}'
    