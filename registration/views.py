import warnings

from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group, GroupManager
from django.contrib.auth import logout, login, authenticate
from .forms import loginUsers, CadastroUsuarios

def authLogin(request):
    if not request.user.is_authenticated:
        if request.POST:
            form = loginUsers(request.POST or None)
            formData = request.POST
            if form.is_valid():
                username = formData['username']
                password = formData['password']
                userLogin = authenticate(username=username, password=password)
                try:
                    if User.objects.get(username=username).is_active == True and userLogin != None:
                        login(request, userLogin)
                        return redirect('index')
                    elif User.objects.get(username=username).is_active == False:
                        messages.warning(request, 'Usuario Desativado! Contate o Administrador!')
                    elif userLogin != None:
                        messages.warning(request, 'Preencha o Usuario ou Senha Corretamente!')
                    else:
                        messages.warning(request, 'Erro de Login! Contate o Administrador!')
                except User.DoesNotExist:
                    messages.warning(request, 'Nome de Usuario ou Senha incorretos!')
            else:
                pass
        else:
            form = loginUsers()
        return render(request, 'authLogin.html', {'form': form})
    else:
        return redirect('index')

def authLogout(request):
    logout(request)
    return redirect(authLogin)

def cadastroUsuarios(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        groups = str(User.objects.get(id=request.user.id).groups.all())
        if 'Acesso' in groups or user.is_staff or user.is_superuser:
            if request.POST:
                form = CadastroUsuarios(request.POST or None)
                formData = request.POST
                if form.is_valid():
                    if formData['password1'] == formData['password2']:
                        pass
                        newuser = User.objects.create_user(
                            username=formData['username'],
                            first_name=formData['first_name'],
                            last_name=formData['last_name'],
                            password=formData['password1'],
                            email=formData['email'],
                            is_active=True,
                        )
                        GroupPerm = Group.objects.get(name='Solicitante')
                        GroupPerm.user_set.add(newuser)
                        GroupPerm.save()
                        newuser.save()
                    else:
                        messages.warning(request, 'Password Incorreto')
                    form = CadastroUsuarios()
                else:
                    messages.warning(request, 'Erro na Criação do Usuário!')
            else:
                form = CadastroUsuarios()
        else:
            return redirect('index')
        return render(request, 'cadastroUsuarios.html', {'form': form})
    else:
        return redirect('auth')

def userPermiss(request):
    return render(request, 'userPermiss.html')