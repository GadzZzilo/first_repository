from django.shortcuts import render
from django.views.generic import ListView

from .models import Human


class HomeView(ListView):
    model = Human
    template_name = "index.html"


class AboutView(ListView):
    model = Human
    template_name = 'inside.html'
