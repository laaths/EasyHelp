from django.forms import ModelForm
from django import forms
from django.core.mail.message import EmailMessage
from django.contrib.auth.models import User


class loginUsers(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


class CadastroUsuarios(forms.Form):
    CHOICES = (('Acesso', 'Acesso'), ('Atendente', 'Atendente'), ('Solicitante', 'Solicitante'))
    first_name = forms.CharField(label='Nome', max_length=20)
    last_name = forms.CharField(label='Sobrenome', max_length=20)
    username = forms.CharField(label='Username', max_length=20)
    email = forms.EmailField(label='E-Mail', initial='@easyhelp.com')
    # is_staff = forms.CharField(label='Pagina de Adminstrador', required=False, widget=forms.CheckboxInput)
    # is_superuser = forms.CharField(label='Super Usuario', required=False, widget=forms.CheckboxInput)
    password1 = forms.CharField(label='Digite a Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Digite a Senha Novamente', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]
