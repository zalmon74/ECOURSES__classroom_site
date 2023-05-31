from django.views.generic import TemplateView


class CoursesList(TemplateView):
    """ Вьюшка для страницы со всеми курсами
    """
    
    template_name = 'training_course/courses_list.html'

