from django.shortcuts import render
from django.views.generic import ListView

from .models import Human


class HomeView(ListView):
    model = Human
    template_name = "home.html"
    context_object_name = 'posts'

    def get_queryset(self):
        return Human.objects.all()


class AboutView(ListView):
    model = Human
    template_name = 'about.html'


class ServicesView(ListView):
    model = Human
    template_name = 'services.html'


class ContactView(ListView):
    model = Human
    template_name = 'contact.html'
