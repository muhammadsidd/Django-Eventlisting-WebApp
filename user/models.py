from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
# Create your models here.


class Role(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

class UserManagement(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    role = models.ForeignKey(Role,null=False, related_name='role',on_delete=models.CASCADE)
