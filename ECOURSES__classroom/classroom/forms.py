from django import forms
from phonenumber_field.formfields import RegionalPhoneNumberWidget

from .models import ContactusModel


class ContactusForm(forms.ModelForm):
        
    class Meta:
        model = ContactusModel
        fields = ('name', 'email', 'phone_number', 'subject', 'message',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control border-0 p-4', 
                    'placeholder': 'Имя'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control border-0 p-4', 
                    'placeholder': 'Email'
                }
            ),
            'phone_number': RegionalPhoneNumberWidget(
                attrs={
                    'class': 'form-control border-0 p-4', 
                    'placeholder': 'Номер телефона'
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control border-0 p-4', 
                    'placeholder': 'Тема'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control border-0 py-3 px-4', 
                    'rows': 5,
                    'placeholder': 'Сообщение'
                }
            ),
        }
