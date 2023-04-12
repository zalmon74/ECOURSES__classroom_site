from typing import Any

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserAuthenticationForm, UserRegistrationModelForm
from .models import CustomUser


class UserRegistrationView(CreateView):
    """ Для регистрации пользователей
    """
    
    form_class = UserRegistrationModelForm
    model = CustomUser
    template_name = 'accounts/user_registration.html'
    success_url = reverse_lazy('user_registration')
    
    def form_valid(self, form: UserRegistrationModelForm) -> HttpResponse:
        # Add group(role)
        form.instance.role = form.cleaned_data['role']
        # base form_valid
        result = super().form_valid(form)
        return result
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # My
        context['title'] = 'Регистрация'
        context['text_button'] = 'Зарегестрироваться'
        return context


class UserLoginView(LoginView):
    """ Авторизация пользователя
    """
    form_class = UserAuthenticationForm
    template_name = 'accounts/user_authorization.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # My
        context['title'] = 'Авторизация'
        context['text_button'] = 'Войти'
        return context


def logout_user(request: HttpRequest) -> HttpResponseRedirect:
    """ Выход пользователя

    Args:
        request (HttpRequest): Запрос

    Returns:
        HttpResponseRedirect: Ответ с перенапревлением
    """
    logout(request)
    return redirect('index')
