from django.http import HttpResponseNotFound
from django.views.generic import ListView, CreateView, DetailView

from .forms import FeedbackForm
from .models import Service, Developer, Feedback
from common.mixins import DataMixin


class HomeView(DataMixin, ListView):
    model = Service
    template_name = "home.html"
    context_object_name = 'posts'

    def get_queryset(self):
        return Service.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Главная')
        return dict(list(context.items()) + list(user_context.items()))


class AboutView(DataMixin, ListView):
    model = Developer
    template_name = 'about.html'
    context_object_name = 'developers'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='О нас')
        return dict(list(context.items()) + list(user_context.items()))


class FeedbackCreateView(DataMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'contact.html'
    success_url = '/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(user_context.items()))


class DetailService(DataMixin, DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'service_detail.html'
    slug_url_kwarg = 'service_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title=context['service'])
        return dict(list(context.items()) + list(user_context.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница пропала</h1>')
