from django.contrib import admin
from clients.models import ClientModel
@admin.register(ClientModel)
class OpenTicketModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'contatoNum', 'contatoSec', 'ContatoNumSec')
    #list_filter = ('name', 'phone', 'email')
# Register your models here.
