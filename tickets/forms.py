from django.forms import ModelForm
from django import forms
from django.core.mail.message import EmailMessage
from .models import OpenTicketModel, historiesForTickets
from datetime import datetime

class OpenTicketForm(ModelForm):
    nome = forms.CharField(label='Nome do Solicitante', max_length=50, min_length=8, initial='LEONARDO TESTE')
    email = forms.EmailField(label='E-mail', max_length=100, initial='teste@teste.com')
    setor = forms.CharField(label='Setor', max_length=50, initial='Setor Teste')
    tel_ramal = forms.CharField(label='Celular / Ramal', max_length=50, min_length=9, initial='51 992878332')
    titulo = forms.CharField(label='Titulo - Problema', max_length=100, min_length=10, initial='Titulo teste')
    dsticket = forms.CharField(label='Descrição do Chamado', widget=forms.Textarea(), max_length=1500, initial='testando a descrição')
    createDate = forms.DateTimeField(label='Data de Abertura', initial=datetime.now(), required=True)

    class Meta:
        model = OpenTicketModel
        fields = ['nome', 'email', 'setor', 'tel_ramal', 'titulo', 'dsticket']

class historiesForTicketsForm(ModelForm):
    dstkHistories = forms.CharField(label='Descrição', required=True, max_length=1500, widget=forms.Textarea)
    encerrar = forms.CharField(label='Encerrar', required=False, widget=forms.CheckboxInput)

    class Meta:
        model = historiesForTickets
        fields = [
            'dstkHistories'
        ]