from statistics import mean
from typing import Any, Dict

from django.views.generic import ListView

from .models import ReviewCourse, TrainingCourseModel


class CoursesList(ListView):
    """ Вьюшка для страницы со всеми курсами
    """
    template_name = 'training_course/courses_list.html'
    model = TrainingCourseModel
    context_object_name = 'all_courses'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """ Формирование контекста

        Returns:
            Dict[str, Any]: Сформированный контекст
        """
        context = super().get_context_data(**kwargs)
        # Дополняем курсы оценкой и количеством отзывов
        for el in context['object_list']:
            reviews_filter = ReviewCourse.objects.filter(course=el.id)
            el.count_review = reviews_filter.count()
            lst_grade = list(reviews_filter.values_list('grade', flat=True))
            el.review_mean_grade = f'{mean(lst_grade if lst_grade else [0]):.2f}'
        context['title'] = 'Курсы'
        
        return context

