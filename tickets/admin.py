from django.contrib import admin
from tickets.models import OpenTicketModel

@admin.register(OpenTicketModel)
class OpenTicketModelAdmin(admin.ModelAdmin):
    list_display = ('id_ticket', 'nome', 'setor', 'titulo')
