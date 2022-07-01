from django.shortcuts import render
from .forms import OpenTicketForm, historiesForTicketsForm, PesquisaTicket
from .models import OpenTicketModel, ticketsForUsers, historiesForTickets
from registration.views import loginUsers
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
from django.utils import timezone
from django.http import HttpResponseRedirect

def baseView(request):
    if request.user.is_authenticated:
        tickets_list_ab = OpenTicketModel.objects.filter(status=0)
        tickets_list_en = OpenTicketModel.objects.filter(status=1)
        context_index = {
            'tickets_list': tickets_list_ab,
            'tickets_list_en': tickets_list_en,
        }
        return render(request, 'index.html', context_index)
    else:
        messages.error(request, 'Efetuar Login Para Continuar!')
        return redirect('auth')

def ticket(request):
    def TabelaRelacional():
        tableRelac = ticketsForUsers.objects.all()
        tableticket = OpenTicketModel.objects.last()
        #tableRelac.create(idGroup=0, idUser=request.user.id, idTicket=tableticket)

    if request.user.is_authenticated:
        if request.POST:
            form = OpenTicketForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Deus Abençoe!')
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
        messages.error(request, 'Efetuar Login Para Continuar!')
        return redirect('auth')

def ticketPage(request, id_ticket):
    def TabelaRelacional():
        tableRelac = historiesForTickets.objects.all()
        tableRelac.create(idTicket=id_ticket, idUser=request.user.id, dstkHistories=request.POST['dstkHistories'])
        print(request.POST)

    def encerrarTicket():
        try:
            ticket = OpenTicketModel.objects.get(id_ticket=id_ticket)
            if request.POST['encerrar']:
                ticket.status = '1'
                ticket.closeDate = timezone.now()
                ticket.save()
            else:
                pass
        except KeyError:
            pass

    if request.user.is_authenticated:
        if request.POST:
            form = historiesForTicketsForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Deus Abençoe!')
                TabelaRelacional()
                encerrarTicket()
                form = historiesForTicketsForm()
                return redirect('index')
            else:
                form = historiesForTicketsForm()
        else:
            form = historiesForTicketsForm()
        tablehistor = historiesForTickets.objects.filter(idTicket=id_ticket)
        tableUser= User.objects.filter().order_by('id')
        context = {
            'ticketObj': OpenTicketModel.objects.get(id_ticket=id_ticket),
            'form': form,
            'tablehistor': tablehistor,
            'tableuser': tableUser,
        }
        return render(request, 'ticketPage.html', context)
    else:
        messages.error(request, 'Efetuar Login Para Continuar!')
        return redirect('auth')

def searchTicket(id_ticket):
    tablehistor = historiesForTickets.objects.filter(idTicket=id_ticket)
    return redirect('ticket', id_ticket)


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
            'modelsbd': OpenTicketModel.objects.filter(nome__exact='TESTANDO'),
        }
        return render(request, 'UserSession.html', context)
    else:
        messages.error(request, 'Efetuar Login Para Continuar!')
        return redirect('auth')