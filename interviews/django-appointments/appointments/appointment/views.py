from django.shortcuts import render, redirect
from .models import Appointment

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
