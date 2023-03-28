from django.urls import path

from .views import *


urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('', HomeView.as_view(), name='home'),
]
