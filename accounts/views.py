from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Contractor, Ticket
from .forms import TicketForm, ContractorForm, CreateUserForm
from .filters import TicketFilter
from django.contrib import messages

# Create your views here

# Login & Register Views
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account ' + user + ' was created successfuly.')
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print(password)

    context = {}
    return render(request, 'accounts/login.html', context)

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

    ticket_filter = TicketFilter(request.GET, queryset=tickets)
    tickets = ticket_filter.qs

    context = {
        'contractor': contractor,
        'tickets': tickets,
        'tickets_count': tickets_count,
        'ticket_filter': ticket_filter
    }
    return render(request, 'accounts/contractors.html', context)

# Create Functions

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

# Update Functions

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

# Delete Functions

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