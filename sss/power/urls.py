from django.urls import path

from .views import *


urlpatterns = [
    path('about', AboutView.as_view(), name='about'),
    path('', HomeView.as_view(), name='home'),
]