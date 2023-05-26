from django.db import models

from .category import Category


class Tag(models.Model):
    """ Описывает Тег на сайте
    """
    name = models.CharField(
        max_length=50, 
        verbose_name='наименование тега', 
        unique=True
    )
    name_visible = models.CharField(
        max_length=50, 
        verbose_name='Наименование тега, которое будет видель пользователи', 
        unique=True
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name='Категория',
        help_text='К какой категории относится тег',
    )
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    
    def __str__(self) -> str:
        return self.name
