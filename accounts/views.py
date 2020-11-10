from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from .models import Contractor, Ticket
from .forms import TicketForm, ContractorForm

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

def tickets(request):
    tickets = Ticket.objects.all()
    context = {
        'tickets': tickets
    }
    return render(request, 'accounts/tickets.html', context)

def contractors(request, pk_id):
    contractor = Contractor.objects.get(id=pk_id)
    tickets = contractor.ticket_set.all()
    tickets_count = tickets.count()
    context = {
        'contractor': contractor,
        'tickets': tickets,
        'tickets_count': tickets_count
    }
    return render(request, 'accounts/contractors.html', context)

def create_ticket(request, pk_id):
    contractor = Contractor.objects.get(id=pk_id)
    form = TicketForm(initial={'contractor': contractor})
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/ticket_form.html', context)

def create_contractor(request):
    form = ContractorForm()
    if request.method == 'POST':
        form = ContractorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/contractor_form.html', context)

def update_ticket(request, pk_id):
    ticket = Ticket.objects.get(id=pk_id)
    form = TicketForm(instance=ticket)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/ticket_form.html', context)

def update_contractor(request, pk_id):
    contractor = Contractor.objects.get(id=pk_id)
    form = ContractorForm(instance=contractor)
    if request.method == 'POST':
        form = ContractorForm(request.POST, instance=contractor)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/contractor_form.html', context)

def delete_ticket(request, pk_id):
    ticket = Ticket.objects.get(id=pk_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('/')

    context = {'ticket': ticket}
    return render(request, 'accounts/delete_ticket.html', context)

def delete_contractor(request, pk_id):
    contractor = Contractor.objects.get(id=pk_id)
    if request.method == 'POST':
        contractor.delete()
        return redirect('/')

    context = {'contractor': contractor}
    return render(request, 'accounts/delete_contractor.html', context)