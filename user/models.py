from django.db import models
from django.contrib.auth.models import User,Group
from django.urls import reverse
from datetime import date


# Create your models here.
class Role(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class UserManagement(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, default=1, on_delete=models.CASCADE)


    def __str__(self):
        return self.user
    