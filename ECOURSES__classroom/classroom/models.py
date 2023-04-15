from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ContactusModel(models.Model):
    """ Хранит сообщения, которые были отправлены через форму "Связаться с нами"
    """
    name = models.CharField(max_length=70, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    phone_number = PhoneNumberField(verbose_name='Номер телефона')
    subject = models.CharField(max_length=70, verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщение')
    sent_date = models.DateField(
        verbose_name='Дата отправления', 
        auto_now_add=True
    )
    
    class Meta:
        verbose_name = 'Сообщение со страницы "Связаться с нами"'
        verbose_name_plural = 'Сообщения со страницы "Связаться с нами"'
        
    def __str__(self) -> str:
        return f'{self.subject} | {self.name} ({self.email})'
