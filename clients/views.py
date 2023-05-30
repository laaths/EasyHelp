from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
from django.utils import timezone
from django.http import HttpResponseRedirect
from .forms import ClientModelForm
from .models import ClientModel

def cadastroClientes(request):
    if request.user.is_authenticated:
        if request.POST:
            form = ClientModelForm(request.POST)
            if form.is_valid():
                form.save()
                form = ClientModelForm()
                return redirect('index')
            else:
                messages.success(request, 'Erro ao Cadastrar Cliente!')
        else:
            form = ClientModelForm()
        return render(
            request, 'cadastroClientes.html',
            {
                'form': form,
                'user': request.user,
            }
        )
    else:
        messages.error(request, 'Efetuar Login Para Continuar!')
        return redirect('auth')
