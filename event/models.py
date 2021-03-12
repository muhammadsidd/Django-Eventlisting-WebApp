from django.utils import timezone
from django.db import models

class Category(models.Model):
    category_type = models.CharField(max_length=100)
    def __str__(self):
        return self.category_type

class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=30)
    image = models.ImageField(upload_to='event', blank=True)
    Category = models.ForeignKey(Category, null=True, related_name='categories', on_delete=models.CASCADE)
    adult_price = models.FloatField(default=0.0)
    child_price = models.FloatField(default=0.0)
    Allow_Registration = models.BooleanField()

    def __str__(self):
        return self.title