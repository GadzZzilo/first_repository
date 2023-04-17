from django.urls import path

from .views import *


urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', FeedbackCreateView.as_view(), name='contact'),
    path('service/<slug:service_slug>', DetailService.as_view(), name='service'),
    path('', HomeView.as_view(), name='home'),
]
