from django.forms import ModelForm
from django import forms
from django.core.mail.message import EmailMessage

class loginUsers(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class CadastroUsuarios(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    nome = forms.CharField(label='Nome', max_length=20)
    sobrenome = forms.CharField(label='Sobrenome', max_length=20)
    email = forms.EmailField(label='E-Mail')
    active = forms.CharField(label='Ativo', widget=forms.CheckboxInput)
    adminpage = forms.CharField(label='Pagina de Adminstrador', widget=forms.CheckboxInput)
    superuser = forms.CharField(label='Super Usuario', widget=forms.CheckboxInput)
    password1 = forms.CharField(label='Digite a Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Digite a Senha Novamente', widget=forms.PasswordInput)