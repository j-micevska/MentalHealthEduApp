from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ("date_posted", "author", )


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Корисничко име'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Е-маил адреса'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Лозинка'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Повтори лозинка'}))