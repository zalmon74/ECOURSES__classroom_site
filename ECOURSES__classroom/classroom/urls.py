from django.urls import path

from .views import *

urlpatterns = [
    path('contactus/', ContactusView.as_view(), name='contact_us'),
    path('', IndexPageView.as_view(), name='index'),
]
