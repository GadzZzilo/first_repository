from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from common.mixins import DataMixin
from .forms import RegisterUserForm, LoginUserForm


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'authentication.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Авторизация', login_flag=True)
        return dict(list(context.items()) + list(user_context.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'authentication.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(user_context.items()))


def logout_user(request):
    logout(request)
    return redirect('home')
