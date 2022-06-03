from django.shortcuts import render
from .forms import OpenTicketForm
from .models import OpenTicketModel
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User


def baseView(request):
    return render(request, 'base.html')

def ticket(request):
    if request.POST:
        form = OpenTicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Deus Abençoe!')
            form = OpenTicketForm()
        else:
            messages.success(request, 'Erro na Abertura do Chamado!')
    else:
        form = OpenTicketForm()

    return render(
        request, 'openTicket.html',
        {
            'form': form,
        }
    )

def UserSession(request):

    context = {
        'request': request,
        'user': User.objects.get(username=request.user),
        'permissions': User.objects.get(username=request.user).get_user_permissions,
        'modelsbd': OpenTicketModel.objects.all(),
    }
    return render(request, 'UserSession.html', context)