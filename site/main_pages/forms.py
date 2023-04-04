from captcha.fields import CaptchaField
from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    # name = forms.CharField(label='Имя', max_length=100, widget=forms.Textarea(attrs={'cols': 30, 'rows': 1}))
    # email = forms.EmailField(label='Email', widget=forms.Textarea(attrs={'cols': 30, 'rows': 1}))
    # message = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(),
            'email': forms.EmailInput(),
            'message': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
