from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

class OpenTicketModel(models.Model):
    id_ticket = models.IntegerField('idticket', primary_key=True, auto_created=True, unique=True)
    nome = models.CharField('nome', max_length=50)
    email = models.EmailField('email', max_length=100)
    setor = models.CharField('Setor', max_length=50)
    tel_ramal = models.CharField('contato', max_length=50)
    titulo = models.CharField('titulo', max_length=100)
    dsticket = models.CharField('dschamado', max_length=1500)
    createDate = models.DateTimeField('createdate', default=timezone.now)
    status = models.FloatField(default=False)

    def __int__(self):
        return self.id_ticket

class ticketsForUsers(models.Model):
    idTicket = models.IntegerField('idticket', unique=True)
    idUser = models.IntegerField('iduser')
    idGroup = models.IntegerField('idgroup')

    def __str__(self):
        return self.id

class historiesForTickets(models.Model):
    idTicket = models.IntegerField('idticket')
    dstkHistories = models.CharField('dsticket', max_length=1500)
    dateHistories = models.DateTimeField('date', auto_created=True)

    def __str__(self):
        return self.id

class TeamsForTicketsusers(models.Model):
    TeamName = models.CharField('nome', max_length=50)