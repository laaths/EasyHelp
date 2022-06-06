from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('auth/', authLogin, name='auth'),
    path('logout/', authLogout, name='logout'),
    path('cadastro', cadastroUsuarios, name='caduser'),
    path('userpermiss', userPermiss, name='userpermiss'),
]