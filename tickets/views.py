from django.shortcuts import render
from .forms import OpenTicket
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User


def baseView(request):
    return render(request, 'base.html')

def ticket(request):
    form = OpenTicket()

    context = {
        'form': form,
    }
    return render(request, 'openTicket.html', context)

def UserSession(request):

    context = {
        'request': request,
        'user': User.objects.get(username=request.user),
        'permissions': User.objects.get(username=request.user).get_user_permissions
    }
    return render(request, 'UserSession.html', context)