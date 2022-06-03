from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User

def authLogin(request):
    return render(request, 'authLogin.html')

def authLogout(request):
    return render(request, 'authLogout.html')

def cadastroUsuarios(request):
    return render(request, 'cadastroUsuarios.html')

def userPermiss(request):
    return render(request, 'userPermiss.html')