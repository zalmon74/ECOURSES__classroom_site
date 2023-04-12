from django import forms
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.safestring import mark_safe

from .models import CustomUser


class UserRegistrationModelForm(UserCreationForm):
    """ Форма для регистрации пользователей
    """
    
    password1 = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control border-0 p-4', 
                'placeholder': 'Пароль',
            }
        ),
    )
    password2 = forms.CharField(
        label='Повтор пароля',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control border-0 p-4', 
                'placeholder': 'Повтор пароля',
            }
        )
    )
    first_name = forms.CharField(
        label='Имя',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-0 p-4', 
                'placeholder': 'Имя',
            }
        )
    )
    second_name = forms.CharField(
        label='Фамилия',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-0 p-4', 
                'placeholder': 'Фамилия',
            }
        )
    )
    surname = forms.CharField(
        label='Отчество',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-0 p-4', 
                'placeholder': 'Отчество'
            }
        )
    )
    role = forms.ChoiceField(
        label='Роль',
        required=True,
        choices=(
            (None, 'Выберите роль'),
            (settings.NAME_DB_NOT_VERIFIED_PARTNER_GROUP, settings.NAME_PARTNER_GROUP),
            (settings.NAME_DB_NOT_VERIFIED_TEACHER_GROUP, settings.NAME_TEACHER_GROUP),
            (settings.NAME_DB_STUDENT_GROUP, settings.NAME_STUDENT_GROUP),
        ),
        widget=forms.Select(
            attrs={'class': 'custom-select', },
        ),
        help_text=mark_safe(
            '<br>'.join([
                'Партнер - создает курсы;', 
                'Учитель - преподает на курсах;', 
                'Студент - обучается на курсах.',
            ])
        )
    )
    
    class Meta:
        model = CustomUser
        fields = (
            'email', 
            'password1', 
            'password2', 
            'first_name', 
            'second_name',
            'surname',
            'role', 
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control border-0 p-4', 
                    'placeholder': 'Email'
                }
            ),
        }


class UserAuthenticationForm(AuthenticationForm):
    """ Форма дла аутентификации пользователя
    """
    
    username = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control border-0 p-4', 
                'placeholder': 'Email',
                'autofocus': ''
            }
        )
    )
    password = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control border-0 p-4', 
                'placeholder': 'Пароль'
            }
        )
    )
    
    class Meta:
        model = CustomUser
