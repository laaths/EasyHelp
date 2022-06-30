from django.contrib import admin
from django.urls import path, include
import tickets
from .views import ticket, UserSession, baseView, ticketPage, RegistroTicket

urlpatterns = [
    path('', baseView, name='index'),
    path('ticket', ticket, name='tickets'),
    path('user', UserSession, name='user'),
    path('tickets/<int:id_ticket>', ticketPage, name='ticket'),
]