from django.urls import include, path

from .views import *

urlpatterns = [
    path(
        'registration/', 
        UserRegistrationView.as_view(), 
        name='user_registration',
    ),
    
] 
