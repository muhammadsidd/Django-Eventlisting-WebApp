from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from event.models import Event

class RegisteredEvent(models.Model):
    adult_quantity = models.IntegerField()
    child_quantity = models.IntegerField()
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, default=1, on_delete=models.CASCADE)

    @property
    def total_value(self, event_id):
        eventx = self.event.objects.get(pk=event_id)
        adult=eventx.adult_price
        child=eventx.child_price
        total = (self.adult_quantity * adult) + (self.child_quantity * child)
        return total


    def __str__(self):
        return str(self.adult_quantity)
    