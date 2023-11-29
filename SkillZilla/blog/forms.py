from django import forms
from django_recaptcha.fields import ReCaptchaField

from .models import Comment


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ['author', 'content',]
