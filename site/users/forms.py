import uuid

from datetime import timedelta
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User
from django.utils.timezone import now

from .models import EmailVerification


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'cols': 30, 'rows': 10}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'cols': '50', 'rows': '10'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'cols': 30, 'rows': 10}))
    email = forms.EmailField(label='Почта',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'cols': 30, 'rows': 10}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'cols': 30, 'rows': 10}))
    password2 = forms.CharField(label='Подтвердите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'cols': 30, 'rows': 10}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=True) # возвращает новосозданный объект пользовтеля
        code = uuid.uuid4()
        expiration = now() + timedelta(hours=48)
        record = EmailVerification.objects.create(code=code, user=user, expiration=expiration)
        record.send_verification_email()
        return user