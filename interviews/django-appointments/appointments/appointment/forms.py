from django import forms
from django.forms import MultiWidget, SplitDateTimeField, DateInput, TimeInput
from django.forms import ModelForm
from .models import Appointment

class SplitDateTimeWidget(MultiWidget):

    def __init__(self, attrs=None, date_format=None, time_format=None):
        widgets = (
                DateInput(attrs={'type': 'date'}, format=date_format),
                TimeInput(attrs={'type': 'time'}, format=time_format),
                )
        super(SplitDateTimeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.date(), value.time().replace(microsecond=0)]
        return [None, None]

class CreateAppointmentForm(ModelForm):
    time = SplitDateTimeField(widget = SplitDateTimeWidget(attrs={'class': 'input-group time'}))
    class Meta:
        model = Appointment
        fields = ['time', 'description']
