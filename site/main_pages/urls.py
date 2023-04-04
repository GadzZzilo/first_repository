from django.urls import path

from .views import *


urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', FeedbackCreateView.as_view(), name='contact'),
    path('', HomeView.as_view(), name='home'),
]
