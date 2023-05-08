from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CheckConstraint, F, Q
from django.utils.safestring import SafeText, mark_safe

from ..help_functions import courses_photo_upload_to
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
    photo = models.ImageField(
        upload_to=courses_photo_upload_to,
        verbose_name='Фото для курса',
        help_text='Изображение, которое будет отображаться в заголовке курса'
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
    
    def image_tag(self) -> SafeText:
        """ Формирует html-тег с изображением

        Returns:
            SafeText: Сформированный тег
        """
        return mark_safe('<img src="%s" width="100" height="50" />' % (self.photo.url))
    
    
class MoreInformationAboutCourses(models.Model):
    """ Дополнительная информация о курсе
    """
    course = models.OneToOneField(
        TrainingCourseModel,
        on_delete=models.PROTECT,
        verbose_name='Курс',
        help_text='Курс, к которому относится дополнительная информация'
    )
    description = models.TextField(verbose_name='Описание курса')
    course_program = models.TextField(
        verbose_name='Программа курса',
        help_text='План, по которому будут заниматься ученики (студенты)',
    )
    
    class Meta:
        verbose_name = 'Дополнительна информация о курсе'
        verbose_name_plural = 'Дополнительна информация о курсах'
    
    def __str__(self) -> str:
        return f'Курс "{self.course.name}" - дополнительная информация'
    

class ReviewCourse(models.Model):
    """ Отзыв к курсу
    """
    course = models.ForeignKey(
        TrainingCourseModel,
        on_delete=models.PROTECT,
        verbose_name='Курс',
        help_text='Курс, к которому пишется отзыв',
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        verbose_name='Автор отзыва'
    )
    grade = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        help_text='Может имееть значение от 1 до 10',
    )
    grade_comment = models.TextField(
        verbose_name='Комментарий',
        help_text='Может быть пустым',
        blank=True,
    )
    f_deleted = models.BooleanField(
        default=False,
        verbose_name='Флаг удаленного комментарий',
        help_text='Устанавливается, когда комментарий удаляется администратором',
    )
    created = models.DateField(
        verbose_name='Дата создания отзыва',
        auto_now_add=True,
    )
    updated = models.DateField(
        verbose_name='Дата последнего редактирования',
        auto_now=True,
    )
    
    class Meta:
        verbose_name = 'Отзыв к курсу'
        verbose_name_plural = 'Отзывы к курсам'
        
        unique_together = ('course', 'author',)
        
        constraints = [
            CheckConstraint(
                check=Q(grade__gt=0) & Q(grade__lt=11),
                name='check_grade__gt_0_and__lt_11',
                violation_error_message='Оценка может иметь диапозон значений от 1 до 10',
            ),            
        ]

    def __str__(self) -> str:
        return f'Отзыв к курсу "{self.course.name}" от "{self.author}"'
