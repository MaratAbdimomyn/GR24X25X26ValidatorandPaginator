from django import forms
from django.forms import ModelForm
from .models import *

class CarForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = ('brand', 'name', 'year')

    def clean_year(self):
        year = self.cleaned_data['year']

        if year < 1900:
            msg = "Модель должна быть старше 1900 года"
            raise forms.ValidationError(msg)
        return year