from django.shortcuts import render
from django.views.generic import ListView

from .models import Service, Developer


class HomeView(ListView):
    model = Service
    template_name = "home.html"
    context_object_name = 'posts'

    def get_queryset(self):
        return Service.objects.all()


class AboutView(ListView):
    model = Developer
    template_name = 'about.html'


class ServicesView(ListView):
    model = Service
    template_name = 'services.html'


class ContactView(ListView):
    model = Service
    template_name = 'contact.html'
