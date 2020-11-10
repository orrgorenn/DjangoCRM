import django_filters
from django_filters import DateFilter, CharFilter

from .models import Ticket, Contractor

class TicketFilter(django_filters.FilterSet):
    created_date = DateFilter(field_name='date_created', lookup_expr='gte')
    closed_date = DateFilter(field_name='date_closed', lookup_expr='lte')
    ticket = CharFilter(field_name='ticket', lookup_expr='icontains')
    class Meta:
        model = Ticket
        fields = ['ticket', 'location', 'status', 'priority']
