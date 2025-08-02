from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
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

def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, id):
    room = Room.objects.get(id=id)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})