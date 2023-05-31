from django.urls import path

from .views import *

urlpatterns = [
    path('', CoursesList.as_view(), name='all_courses'),
]
