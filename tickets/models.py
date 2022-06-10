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
    idTicket = models.ForeignKey(OpenTicketModel, related_name='idticket', on_delete=models.CASCADE)
    #idTicket = models.ForeignKey(User, auto_created=True, unique=True, on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, models.CASCADE, related_name='iduser',)

    def __str__(self):
        return self.id

