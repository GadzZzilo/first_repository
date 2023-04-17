from captcha.fields import CaptchaField, CaptchaTextInput
from django import forms

from .models import Feedback, Service, Developer


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'cols': '30', 'rows': '10'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'cols': '50', 'rows': '10'})
    )
    service = forms.ModelChoiceField(
        label='Выберите услугу, о которой хотите оставить отзыв',
        # widget=forms.TextInput(attrs={'class': 'form-control'}),
        queryset=Service.objects.all(),
        widget=(forms.Select(attrs={'class': 'form-control'})),
        required=False,
        empty_label='Не выбрано'

    )
    author = forms.ModelChoiceField(
        label='Выберите автора, который курировал вас',
        queryset=Developer.objects.all(),
        widget=(forms.Select(attrs={'class': 'form-control'})),
        required=False,
        empty_label='Не выбрано'
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
        fields = ('name', 'email', 'service', 'author', 'message')
