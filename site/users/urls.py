from django.urls import path

from .views import LoginUser, RegisterUser, logout_user, EmailVerificationView

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout', logout_user, name='logout'),
    path('verification/<str:email>/<uuid:code>', EmailVerificationView.as_view(), name='verification'),
]