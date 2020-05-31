from django.contrib import admin

# MANUALLY
from django.urls import path
from .views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view()),
]

# MANUALLY ENDS