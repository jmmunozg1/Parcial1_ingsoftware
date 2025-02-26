from django.db import models

# Create your models here.
class Flight(models.Model):

    FLIGHT_TYPES = [
        ('NAC', 'Nacional'),
        ('INT', 'Internacional'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100, choices=FLIGHT_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
