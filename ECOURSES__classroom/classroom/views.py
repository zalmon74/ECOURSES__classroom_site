from typing import Any

from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import ContactusForm
from .models import ContactusModel


class IndexPageView(TemplateView):
    template_name = 'classroom/index.html'



class ContactusView(CreateView):
    template_name = 'classroom/contact_us.html'
    model = ContactusModel
    form_class = ContactusForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # My
        context['title'] = 'Связаться с нами'
        context['text_button'] = 'Отправить'
        return context
