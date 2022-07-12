from django.shortcuts import render
from .forms import OpenTicketForm, historiesForTicketsForm, PesquisaTicket
from .models import OpenTicketModel, ticketsForUsersRun, historiesForTickets
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
        tickets_list_ea = OpenTicketModel.objects.filter(status=2)
        tickets_list_en = OpenTicketModel.objects.filter(status=1)
        context_index = {
            'tickets_list': tickets_list_ab,
            'tickets_list_en': tickets_list_en,
            'tickets_list_ea': tickets_list_ea,
        }
        return render(request, 'index.html', context_index)
    else:
        messages.error(request, 'Efetuar Login Para Continuar!')
        return redirect('auth')

def ticket(request):
    def TabelaRelacionalTicketsForUsers(id_ticket):
        tkrun = ticketsForUsersRun.objects.all()
        tkrun.create(idGroup=0, idUser=request.user.id, idTicket=id_ticket)

    if request.user.is_authenticated:
        if request.POST:
            form = OpenTicketForm(request.POST)
            if form.is_valid():
                form.save()
                form = OpenTicketForm()
                tkopen = OpenTicketModel.objects.last()
                TabelaRelacionalTicketsForUsers(tkopen)
            else:
                messages.success(request, 'Erro na Abertura do Chamado!')
        else:
            form = OpenTicketForm()
        return render(
            request, 'openTicket.html',
            {
                'form': form,
                'user': request.user,
            }
        )
    else:
        messages.error(request, 'Efetuar Login Para Continuar!')
        return redirect('auth')

def ticketPage(request, id_ticket):
    def TabelaRelacionalTicketsForUsers():
        tableRelac = ticketsForUsersRun.objects.all()
        tableRelac.create(idGroup=0, idUser=request.user.id, idTicket=id_ticket)

    def TabelaRelacional(obj_all, dstkHistories):
        obj_all.create(idTicket=id_ticket, idUser=request.user.id, dstkHistories=dstkHistories)
        print(request.POST)

    def iniciarAtendimento():
        try:
            ticket = OpenTicketModel.objects.get(id_ticket=id_ticket)
            if request.POST:
                ticket.status = '2'
                tableRelac = historiesForTickets.objects.all()
                TabelaRelacional(tableRelac, "Atendimento Inciado")
                ticket.save()
            else:
                pass
        except KeyError:
            pass

    def encerrarTicket():
        try:
            ticket = OpenTicketModel.objects.get(id_ticket=id_ticket)
            if request.POST['encerrar'] == "":
                ticket.status = '1'
                ticket.closeDate = timezone.now()
                ticket.save()
            else:
                pass
        except KeyError:
            print('teste')

    def reabrirTicket():
        try:
            ticket = OpenTicketModel.objects.get(id_ticket=id_ticket)
            if request.GET:
                ticket.status = '2'
                tableRelac = historiesForTickets.objects.all()
                TabelaRelacional(tableRelac, 'Ticket Reaberto')
                ticket.save()
            else:
                pass
        except KeyError:
            pass

    if request.user.is_authenticated:
        if request.POST:
            form = historiesForTicketsForm(request.POST)
            if form.is_valid():
                tableRelac = historiesForTickets.objects.all()
                TabelaRelacional(tableRelac, request.POST['dstkHistories'])
                encerrarTicket()
                form = historiesForTicketsForm()
                return redirect('index')
            else:
                iniciarAtendimento()
                #form = historiesForTicketsForm()
        elif request.GET:
            reabrirTicket()
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

def buscarTicket(id_ticket):
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