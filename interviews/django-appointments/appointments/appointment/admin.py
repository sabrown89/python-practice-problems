from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('time','description')

admin.site.register(Appointment, AppointmentAdmin)
