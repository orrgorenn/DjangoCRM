from django.shortcuts import render
from django.http import HttpResponse

# Create your views here

def home(request):
    return render(request, 'accounts/dashboard.html')

def tickets(request):
    return render(request, 'accounts/tickets.html')

def contractors(request):
    return render(request, 'accounts/contractors.html')
