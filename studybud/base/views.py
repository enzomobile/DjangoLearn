from django.shortcuts import render
from django.http import HttpResponse # HttpResponse for routing simple responses.

def home(request):
    return HttpResponse("Home page") # This is a simple view function that returns a response for the home page.

def room(request):
    return HttpResponse("Room page") # This is a simple view function that returns a response for the room page.
