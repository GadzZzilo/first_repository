from django.http import HttpResponseNotFound
from django.views.generic import ListView, CreateView, DetailView

from .forms import FeedbackForm
from .models import Service, Developer, Feedback
from common.mixins import DataMixin


class HomeView(DataMixin, ListView):
    model = Service
    template_name = "home.html"
    context_object_name = 'posts'
    title = 'Главная'

    def get_queryset(self):
        return Service.objects.all()


class AboutView(DataMixin, ListView):
    model = Developer
    template_name = 'about.html'
    context_object_name = 'developers'
    title = 'О нас'


class FeedbackCreateView(DataMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'contact.html'
    success_url = '/'
    title = 'Обратная связь'


class DetailService(DataMixin, DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'service_detail.html'
    slug_url_kwarg = 'service_slug'
    title = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['service']
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница пропала</h1>')
