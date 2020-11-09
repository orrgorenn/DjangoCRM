from django.db import models

# Create your models here.
class Contractor(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100, null=False)
    cellphone = models.CharField(max_length=15, null=True)
    office_phone = models.CharField(max_length=15, null=True)
    field_of_work = models.CharField(max_length=50, null=False, default='NaN')
    date_created = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.last_name + ' ' + self.first_name

class Ticket(models.Model):
    ticket = models.CharField(max_length=100, null=False)
    CATEGORY_CHOICES = [
        ('1', 'איטום'),
        ('2', 'אינסטלציה'),
        ('3', 'אקוסטיקה'),
        ('4', 'ביטחון'),
        ('5', 'בטיחות - אש'),
        ('6', 'בטיחות - אתר'),
        ('7', 'בינוי'),
        ('8', 'חשמל'),
        ('9', 'מיזוג אוויר'),
        ('10', 'נגישות'),
        ('11', 'ניקיון'),
        ('12', 'תאורה'),
        ('13', 'תקשורת')
    ]
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='1')
    LOCATION_CHOICES = [
        ('P5', 'Parking 5'),
        ('P4', 'Parking 4'),
        ('P3', 'Parking 3'),
        ('P2', 'Parking 2'),
        ('P1', 'Parking 1'),
        ('GRND', 'Ground'),
        ('F1', 'Floor 1'),
        ('F2', 'Floor 2'),
        ('F3', 'Floor 3'),
        ('F4', 'Floor 4'),
        ('F5', 'Floor 5'),
        ('F6', 'Floor 6'),
        ('F7', 'Floor 7'),
        ('F8', 'Floor 8'),
        ('ROOF', 'Roof')
    ]
    location = models.CharField(max_length=4, choices=LOCATION_CHOICES, default='GRND')
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('WTNG', 'Waiting'),
        ('OPEN', 'Opened'),
        ('RSPD', 'Responded'),
        ('NATN', 'Needs Attention'),
        ('CLSD', 'Closed')
    ]
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='NEW')
    priority = models.IntegerField(null=False, default=1)
    contractor = models.ForeignKey(Contractor, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    date_last_update = models.DateTimeField(null=True)
    date_closed = models.DateTimeField(null=True)

    def __str__(self):
        return self.ticket