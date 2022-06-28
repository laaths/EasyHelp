from django.forms import ModelForm
from django import forms
from django.core.mail.message import EmailMessage
from .models import OpenTicketModel
from datetime import datetime

class OpenTicketForm(ModelForm):
    nome = forms.CharField(label='Nome', max_length=50, min_length=8)
    email = forms.EmailField(label='E-mail', max_length=100)
    setor = forms.CharField(label='Setor', max_length=50)
    tel_ramal = forms.CharField(label='Celular / Ramal', max_length=50, min_length=9)
    titulo = forms.CharField(label='Titulo - Problema', max_length=100, min_length=10)
    dsticket = forms.CharField(label='Descrição do Chamado', widget=forms.Textarea(), max_length=1500)
    createDate = forms.DateTimeField(initial=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), required=False)

    class Meta:
        model = OpenTicketModel
        fields = ['nome', 'email', 'setor', 'tel_ramal', 'titulo', 'dsticket']

class MetaModelTicket(forms.ModelForm):
    pass