from django.shortcuts import render
from django.http import HttpResponse

# Create your views here

def home(request):
    return HttpResponse('Home Page')

def tickets(request):
    return HttpResponse('Tickets Page')

def contractors(request):
    return HttpResponse('Contractors Page')
