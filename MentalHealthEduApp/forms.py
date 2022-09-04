from django import forms
from .models import Message
from django.contrib.auth.models import User


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ("date_posted", "author", )