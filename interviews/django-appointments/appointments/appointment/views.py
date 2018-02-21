from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment
from .forms import CreateAppointmentForm
from django.core import serializers

def index(request):
    return render(request, 'appointment/index.html')

def search_appointments(request):
    if request.method == 'GET' and 'search_text' in request.GET:
        search_text = request.GET['search_text']
        if search_text:
            appointments = Appointment.objects.filter(description__contains=search_text)
            appointments.search = True
#            appointments = serializers.serialize('json', Appointment.objects.filter(description__contains=search_text))
        else:
            appointments = Appointment.objects.all()
            appointments.search = False
#            appointments = serializers.serialize('json', Appointment.objects.all())

    return render(request, 'appointment/ajax_search.html', {'appointments': appointments})
#    return render(request, 'appointment/json_table.html', {'appointments': appointments})

def create_form(request):
    form_class = CreateAppointmentForm
    return render(request, 'appointment/ajax_create_form.html', {'form': form_class})

def create(request):
    if request.method == "POST":
        form = CreateAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment was successfully added')
            return redirect('/')
        return render(request, 'appointment/ajax_create_form.html', {'form': form})
