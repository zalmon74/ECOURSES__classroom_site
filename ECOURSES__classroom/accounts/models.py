from django.contrib.auth.models import AbstractUser
from django.db import models

from .help_functions import user_photo_upload_to
from .managers import CustomUserManager
from .validators import *


class CustomUser(AbstractUser):
    """ Перегруженная модель пользователя
    """
    username = None
    
    email = models.EmailField(unique=True, db_index=True, verbose_name='Email')
    mail_confirmation = models.BooleanField(
        default=False,
        verbose_name='Подтверждение почты'
    )
    first_name = models.CharField(
        max_length=50,
        validators=[validation_first_second_sur_name, ],
        verbose_name='Имя',
        help_text='Имя пользователя может иметь максимум 50 символов и содержать только русские и латинские буквы'
    )
    second_name = models.CharField(
        max_length=50,
        validators=[validation_first_second_sur_name, ],
        verbose_name='Фамилия',
        help_text='Фамилия пользователя может иметь максимум 50 символов и содержать только русские и латинские буквы'
    )
    surname = models.CharField(
        max_length=50,
        validators=[validation_first_second_sur_name, ],
        verbose_name='Отчество',
        help_text='Отчество пользователя может иметь максимум 50 символов и содержать только русские и латинские буквы',
        default='',
    )
    
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['password', 'first_name', 'second_name', ]

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    def get_full_name(self) -> str:
        return ' '.join([name for name in [
            self.first_name,
            self.second_name,
            self.last_name
        ] if name])
    
    def get_full_name_with_email(self) -> str:
        return self.get_full_name() + f' ({self.email})'
    

class UserPhoto(models.Model):
    """ Содержит фотографии для профиля пользователя
    """
    user = models.OneToOneField(
        CustomUser,
        models.PROTECT,
        db_index=True,
        verbose_name='Пользователь',
    )
    photo = models.ImageField(
        upload_to=user_photo_upload_to,
        verbose_name='Фотография пользователя',
    )
    
    class Meta:
        verbose_name = 'Фото пользователя'
        verbose_name_plural = 'Фото пользователей'
    
    def __str__(self) -> str:
        return self.user.get_full_name_with_email()
    