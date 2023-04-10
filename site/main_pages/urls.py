from django.urls import path

from .views import *


urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', FeedbackCreateView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout', logout_user, name='logout'),
    path('service/<slug:service_slug>', DetailService.as_view(), name='service'),
    path('', HomeView.as_view(), name='home'),
]
