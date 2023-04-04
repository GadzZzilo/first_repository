from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, DetailView

from .forms import FeedbackForm
from .models import Service, Developer, Feedback


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


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'contact.html'
    success_url = '/'
