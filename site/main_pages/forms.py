from captcha.fields import CaptchaField, CaptchaTextInput
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '30', 'rows': '10'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'cols': '50', 'rows': '10'})
    )
    message = forms.CharField(
        label='Отзыв',
        widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 10})
    )
    captcha = CaptchaField(
        label='Введите текст с картинки:',
        widget=CaptchaTextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'message')
        # widgets = {
        #     'name': forms.Textarea(attrs={'class': 'col-md-6 field', 'label': 'Имя', 'cols': 50, 'rows': 1}),
        #     'email': forms.EmailInput(attrs={'class': 'col-md-6 field', 'label': 'Email'}),
        #     'message': forms.Textarea(attrs={'class': 'col-md-12 field', 'label': 'Отзыв'}),
        # }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'cols': '20', 'rows': '10'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '30', 'rows': '10'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control', 'cols': '30', 'rows': '10'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'cols': '30', 'rows': '10'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'cols': '30', 'rows': '10'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
