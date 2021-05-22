from django import forms
from django.contrib.admin import widgets
from .models import logs


class DateInput(forms.DateInput):
    input_type = 'date'


class checkout(forms.ModelForm):
    class Meta:
        model = logs
        fields = 'rentedDate','returnDate'
        widgets = {
            'rentedDate': DateInput(),
            'returnDate': DateInput(),

        }


