from django.db import models

class ClientModel(models.Model):
    nome = models.CharField('Nome Completo', max_length=100, null=False)
    email = models.EmailField('Email', max_length=150, unique=True)
    contatoNum = models.CharField('Telefone', max_length=20)
    dataNasc = models.DateField('Data de Nascimento')
    cpf = models.CharField('CPF', max_length=11, unique=True)
    cep = models.CharField('CEP', max_length=30)
    cidade = models.CharField('Cidade', max_length=150)
    estado = models.CharField('Estado', max_length=150)
    rua = models.CharField('Rua', max_length=150)
    numero = models.CharField('Numero', max_length=8)
    complemento = models.CharField('Complemento', max_length=250)
    contatoSec = models.CharField('Nome Contato Secundario', max_length=100)
    ContatoNumSec = models.CharField('Numero Contato Secundario', max_length=20)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome