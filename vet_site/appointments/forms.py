# appointments/forms.py

from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['pet', 'date', 'service', 'additional_info', 'emergency_contact']
