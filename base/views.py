from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

#rooms = [
#   {'id':1, 'name':'Lets learn python!'},
#   {'id':2, 'name':'Designs with me'},
#   {'id':3, 'name':'Fronetend developers'}
#]

def home(request):
    rooms = Room.objects.all()
    contex = {'rooms': rooms}
    return render(request, 'base/home.html', contex)

def room(request, id):
    room = Room.objects.get(id=id)
    context = {'room': room}
    return render(request, 'base/room.html', context)