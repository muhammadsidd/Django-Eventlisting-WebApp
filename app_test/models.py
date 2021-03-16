from django.utils import timezone
from django.db import models


class Eventtt(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
