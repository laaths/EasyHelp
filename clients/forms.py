from django.forms import ModelForm, TextInput, EmailInput, DateInput, DateField
from django import forms
from clients.models import ClientModel
from django.core.mail.message import EmailMessage
from datetime import datetime

class ClientModelForm(ModelForm):
    class Meta:
        model = ClientModel
        exclude = ['created_at']
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'contatoNum': TextInput(attrs={'class': 'form-control'}),
            'dataNasc': DateInput(format=('%d-%m-%Y'), attrs={'class': 'form-control'}),
            'cpf': TextInput(attrs={'class': 'form-control'}),
            'cep': TextInput(attrs={'class': 'form-control'}),
            'cidade': TextInput(attrs={'class': 'form-control'}),
            'estado': TextInput(attrs={'class': 'form-control'}),
            'rua': TextInput(attrs={'class': 'form-control'}),
            'numero': TextInput(attrs={'class': 'form-control'}),
            'complemento': TextInput(attrs={'class': 'form-control'}),
            'contatoSec': TextInput(attrs={'class': 'form-control'}),
            'ContatoNumSec': TextInput(attrs={'class': 'form-control'})
        }