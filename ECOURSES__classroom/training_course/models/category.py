from django.db import models
from django.utils.safestring import SafeText, mark_safe

from ..help_functions import category_photo_upload_to


class Category(models.Model):
    """ Описывает категории на сайте
    """
    name = models.CharField(
        max_length=50, 
        verbose_name='Название категории', 
        unique=True
    )
    name_visible = models.CharField(
        max_length=50, 
        verbose_name='Название категории, которое будут видеть пользователи', 
        unique=True
    )
    photo = models.ImageField(
        upload_to=category_photo_upload_to,
        verbose_name='Фото для главной страницы',
    )
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self) -> str:
        return self.name
    
    def image_tag(self) -> SafeText:
        """ Формирует html-тег с изображением

        Returns:
            SafeText: Сформированный тег
        """
        return mark_safe('<img src="%s" width="100" height="50" />' % (self.photo.url))
