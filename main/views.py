import random

from django.views.generic import TemplateView


class MainView(TemplateView):
    """Главная страница"""
    template_name = 'main/main.html'
    extra_context = {
        'title': 'skiPay: Главная страница'
    }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context
