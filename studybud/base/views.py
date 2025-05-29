from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Lets learn Python!'},
    {'id': 2, 'name': 'Design with me!'},
    {'id': 3, 'name': 'Back-End dev!'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)  # Render the home page using a template.

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}

    return render(request, 'base/room.html', context)  # Render the room page using a template.
