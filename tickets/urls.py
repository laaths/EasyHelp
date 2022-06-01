from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', baseView, name='index'),
    path('ticket', ticket, name='tickets'),
    path('user', UserSession, name='user'),
]