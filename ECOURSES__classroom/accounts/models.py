from django.contrib.auth.models import AbstractUser
from django.db import models

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
        help_text='Фамилия пользователя может иметь максимум 50 символов и содержать только русские буквы'
    )
    surname = models.CharField(
        max_length=50,
        validators=[validation_first_second_sur_name, ],
        verbose_name='Отчество',
        help_text='Отчество пользователя может иметь максимум 50 символов и содержать только русские буквы',
        default='',
    )
    
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['password', 'first_name', 'second_name', ]

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
