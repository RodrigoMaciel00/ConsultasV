# appointments/models.py

from django.db import models
from accounts.models import CustomUser

class Pet(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=50)

class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateTimeField()
    service = models.CharField(max_length=200)
    additional_info = models.TextField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=100)

    class Meta:
        unique_together = ('date', 'pet')
