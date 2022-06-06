from django.forms import ModelForm
from django import forms
from django.core.mail.message import EmailMessage

class loginUsers(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
