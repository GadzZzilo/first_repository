from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, DetailView

from .forms import FeedbackForm, LoginUserForm, RegisterUserForm
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
    context_object_name = 'developers'


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'contact.html'
    success_url = '/'


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


def logout_user(request):
    logout(request)
    return redirect('home')


class DetailService(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'service_detail.html'
    slug_url_kwarg = 'service_slug'
