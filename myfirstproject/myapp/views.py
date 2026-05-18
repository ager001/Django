from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Users

def myapp(request):
    users = Users.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))

def details(request,id):
    user = Users.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myapp': user,
    }
    return HttpResponse(template.render(context, request))