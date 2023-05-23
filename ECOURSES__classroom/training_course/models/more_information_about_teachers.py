from django.contrib.auth import get_user_model
from django.db import models

from .category import Category


class MoreInformationAboutTeachers(models.Model):
    """ Описывает дополнительную информацию для учителей
    """
    user = models.OneToOneField(
        get_user_model(), 
        models.PROTECT,
        verbose_name='Пользователь',
    )
    category = models.ForeignKey(
        Category,
        models.PROTECT,
        verbose_name='Категория',
        help_text='Категория, по которой учителя преподают',
    )
    profession = models.CharField(max_length=150, verbose_name='Профессия')
    education = models.TextField(verbose_name='Образование', blank=True)
    experience = models.TextField(verbose_name='Опыт работы', blank=True)
    completed_courses = models.TextField(
        verbose_name='Пройденные курсы',
        help_text='Курсы, необходимо указать, которые не были пройдены в рамках данной платформы',
        blank=True
    )
    previously_supervised_courses = models.TextField(
        verbose_name='Курсы, которые уже преподовали',
        blank=True,
    )
    
    class Meta:
        verbose_name = 'Дополнительные данные для преподователей'
        verbose_name_plural = 'Дополнительные данные для преподователей'

    def __str__(self) -> str:
        return f'Дополнительная информация для преподователей пользователя {self.user.get_full_name()}'
