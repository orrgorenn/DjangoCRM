from django import forms
from .models import Ticket, Contractor

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket', 'category', 'location', 'status', 'priority', 'contractor']

        widgets = {
            'ticket': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'contractor': forms.Select(attrs={'class': 'form-control'})
        }

class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ['first_name', 'last_name', 'email', 'cellphone', 'office_phone', 'field_of_work']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'cellphone': forms.TextInput(attrs={'class': 'form-control'}),
            'office_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'field_of_work': forms.Select(attrs={'class': 'form-control'})
        }