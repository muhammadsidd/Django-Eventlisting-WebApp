from django.db import models
from event.models import Event


class Registration(models.Model):
    event = models.ForeignKey(Event, null= True, related_name='registration_items', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    quantity_adult = models.IntegerField(default=1)
    quantity_child = models.IntegerField(default=0)

