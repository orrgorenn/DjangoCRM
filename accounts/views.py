from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from .models import Contractor, Ticket

# Create your views here

def home(request):
    tickets_var = Ticket.objects.all()
    contractors_var = Contractor.objects.all()
    total_tickets = tickets_var.count()
    resolved_tickets = tickets_var.filter(status='CLSD').count()
    opened_tickets = tickets_var.filter(Q(status='NEW') | Q(status='OPEN') | Q(status='RSPD') | Q(status='NATN')).count()

    context = {
        'tickets': tickets_var,
        'contractors': contractors_var,
        'total_tickets': total_tickets,
        'resolved_tickets': resolved_tickets,
        'opened_tickets': opened_tickets
    }

    return render(request, 'accounts/dashboard.html', context)

def tickets(request, pk_id):
    ticket = Ticket.objects.get(id=pk_id)
    context = {
        'ticket': ticket
    }
    return render(request, 'accounts/tickets.html', context)

def contractors(request, pk_id):
    contractor = Contractor.objects.get(id=pk_id)
    return render(request, 'accounts/contractors.html', {'contractor': contractor})