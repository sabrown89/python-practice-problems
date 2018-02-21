from django.db import models
from django.utils import timezone

class Appointment(models.Model):
    time = models.DateTimeField(default=timezone.now)
    description = models.TextField()

