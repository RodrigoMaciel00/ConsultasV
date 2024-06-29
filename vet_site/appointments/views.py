# appointments/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment, Pet
from .forms import AppointmentForm

@login_required
def schedule(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.owner = request.user
            appointment.save()
            return redirect('schedule')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/schedule.html', {'form': form})
