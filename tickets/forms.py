from django.forms import ModelForm
from django import forms
from django.core.mail.message import EmailMessage

from .models import OpenTicketModel, historiesForTickets
from datetime import datetime
CHOICES = (('ERROS E PROBLEMAS', 'ERROS E PROBLEMAS'), ('SOLICITACOES', 'SOLICITACOES'), ('MELHORIAS', 'MELHORIAS'))

class OpenTicketForm(ModelForm):
    nome = forms.CharField(label='Nome do Solicitante', max_length=50, min_length=8)
    email = forms.EmailField(label='E-mail', max_length=100)
    setor = forms.CharField(label='Setor', max_length=50)
    tel_ramal = forms.CharField(label='Celular / Ramal', max_length=50, min_length=4)
    #titulo = forms.CharField(label='Titulo - Problema', max_length=100, min_length=10, initial='Titulo teste')
    titulo = forms.ChoiceField(label='Titulo - Problema', choices=CHOICES)
    dsticket = forms.CharField(label='Descrição do Chamado', widget=forms.Textarea(), max_length=1500)
    createDate = forms.DateTimeField(label='Data de Abertura', initial=datetime.now(), required=True)

    class Meta:
        model = OpenTicketModel
        fields = ['nome', 'email', 'setor', 'tel_ramal', 'titulo', 'dsticket']

class historiesForTicketsForm(ModelForm):
    dstkHistories = forms.CharField(label='Descrição', required=True, max_length=1500, widget=forms.Textarea)
    #encerrar = forms.CharField(label='Encerrar', widget=forms,required=False)

    class Meta:
        model = historiesForTickets
        fields = [
            'dstkHistories'
        ]

class PesquisaTicket(forms.Form):
    ticketNum = forms.CharField(label='Ticket', max_length=10)