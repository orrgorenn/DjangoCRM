from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseForbidden
from django.contrib.auth.models import Group

from .decorators import unauth_user, allowed_users, admin_only
from .models import Contractor, Ticket
from .forms import TicketForm, ContractorForm, CreateUserForm
from .filters import TicketFilter

# Create your views here

# Login & Register Views
@unauth_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # Add User to 'users' Group
            group = Group.objects.get(name='users')
            user.groups.add(group)
            Contractor.objects.create(
                user = user
            )
            
            messages.success(request, 'Account ' + username + ' was created successfuly.')
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@unauth_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect.')

    context = {}
    return render(request, 'accounts/login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    tickets_var = Ticket.objects.all()
    contractors_var = Contractor.objects.all()
    total_tickets = tickets_var.count()
    resolved_tickets = tickets_var.filter(status='CLSD').count()
    opened_tickets = tickets_var.filter(Q(status='NEW') | Q(status='WTNG') | Q(status='OPEN') | Q(status='RSPD') | Q(status='NATN')).count()

    context = {
        'tickets': tickets_var,
        'contractors': contractors_var,
        'total_tickets': total_tickets,
        'resolved_tickets': resolved_tickets,
        'opened_tickets': opened_tickets
    }

    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def tickets(request):
    tickets = Ticket.objects.all()
    context = {
        'tickets': tickets
    }
    return render(request, 'accounts/tickets.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def userPage(request):
    tickets = request.user.contractor.ticket_set.all()

    total_tickets = tickets.count()
    resolved_tickets = tickets.filter(status='CLSD').count()
    opened_tickets = tickets.filter(Q(status='NEW') | Q(status='WTNG') | Q(status='OPEN') | Q(status='RSPD') | Q(status='NATN')).count()

    print(tickets)
    context = {'tickets': tickets, 'total_tickets': total_tickets, 'resolved_tickets': resolved_tickets, 'opened_tickets': opened_tickets}
    return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def accSettings(request):
    contractor = request.user
    form = ContractorForm(instance=contractor)

    if request.method == 'POST':
        form = ContractorForm(request.POST, request.FILES, instance=contractor)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/acc_settings.html', context)

# Create Functions

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def delete_ticket(request, pk_id):
    ticket = Ticket.objects.get(id=pk_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('/')

    context = {'ticket': ticket}
    return render(request, 'accounts/delete_ticket.html', context)

@login_required(login_url='login')
def delete_contractor(request, pk_id):
    contractor = Contractor.objects.get(id=pk_id)
    if request.method == 'POST':
        contractor.delete()
        return redirect('/')

    context = {'contractor': contractor}
    return render(request, 'accounts/delete_contractor.html', context)