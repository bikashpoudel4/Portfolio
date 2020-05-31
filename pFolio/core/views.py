from django.shortcuts import render

# MANUALLY INSERTED
from django.views.generic import TemplateView
from .models import *

# MANULLY INSERTED
# creating views
class HomeTemplateView(TemplateView):
    template_name = 'home.html'

#     Override get context data method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)#first, call super get context data
        context['about'] = About.objects.first()
        context['services']= Service.objects.all()
        context['works'] = RecentWork.objects.all()
        return context

