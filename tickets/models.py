from django.db import models
from django.contrib.auth.models import User

class OpenTicketModel(models.Model):
    nome = models.CharField('nome', max_length=50)
    email = models.EmailField('email', max_length=100)
    setor = models.CharField('Setor', max_length=50)
    tel_ramal = models.CharField('contato', max_length=50)
    titulo = models.CharField('titulo', max_length=100)
    dsticket = models.CharField('dschamado', max_length=1500)

    def __str__(self):
        return self.nome

class ticketsForUsers(models.Model):
    idTicket = models.IntegerField('idticket', unique=True)
    idUser = models.IntegerField('iduser')
    idGroup = models.IntegerField('idgroup')

    def __str__(self):
        return self.id

