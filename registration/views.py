from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from .forms import loginUsers

def authLogin(request):
    form = loginUsers(request.POST or None)
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                messages.warning(request, 'Conta desativada! Contate o Administrador!')
        # Retorna uma mensagem de erro de 'conta desabilitada' .
        else:
            messages.error(request, 'Usuario ou Senha incorretos!')
        # Retorna uma mensagem de erro 'login inválido'.
        return render(request, 'authLogin.html', {'form': form})
    except KeyError:
        print('try: teste')
        return render(request, 'authLogin.html', {'form': form})

def authLogout(request):
    logout(request)
    return redirect(authLogin)

def cadastroUsuarios(request):
    return render(request, 'cadastroUsuarios.html')

def userPermiss(request):
    return render(request, 'userPermiss.html')