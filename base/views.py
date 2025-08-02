from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id':1, 'name':'Lets learn python!'},
    {'id':2, 'name':'Designs with me'},
    {'id':3, 'name':'Fronetend developers'}
]
def home(request):
    contex = {'rooms': rooms}
    return render(request, 'base/home.html', contex)

def room(request, id):
    room = None
    for i in rooms:
        if i['id'] == int(id):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)