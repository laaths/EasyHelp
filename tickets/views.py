from django.shortcuts import render
from .forms import OpenTicketForm
from .models import OpenTicketModel, ticketsForUsers
from registration.views import loginUsers
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group


def baseView(request):
    return render(request, 'base.html')

def ticket(request):
    def TabelaRelacional():
        tableRelac = ticketsForUsers.objects.all()
        tableticket = OpenTicketModel.objects.get(dsticket=request.POST('dsticket'))
        tableRelac.create(idGroup=0, idUser=request.user.id, idTicket=tableticket('id'))

    if request.user.is_authenticated:
        if request.POST:
            form = OpenTicketForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Deus Abençoe!')
                OpenTicketModel.objects.get(dsticket=request.POST('dsticket'))
                #TabelaRelacional()
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
    else:
        messages.error(request, 'Usuario não Autenticado!')
        return redirect('auth')

def UserSession(request):
    if request.user.is_authenticated:
        #permissions = User.objects.get(username=request.user).user_permissions.values_list('name')
        permissions = request.user.get_user_permissions()
        if len(permissions) == 0:
            permissions = 'Null'
        else:
            pass
        context = {
            'request': request,
            'user': User.objects.get(username=request.user),
            'permissions': permissions,
            'groupsperm': User.objects.get(username=request.user).groups.values_list('name'),
            'modelsbd': OpenTicketModel.objects.all(),
        }
        return render(request, 'UserSession.html', context)
    else:
        messages.error(request, 'Efetuar Login Para Continuar!')
        return redirect('auth')