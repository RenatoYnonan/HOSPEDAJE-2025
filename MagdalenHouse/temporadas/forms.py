from django import forms
from django.forms import widgets
from .models import *

class FormsTemporadas(forms.ModelForm):
    class Meta:
        model = Temporada
        fields = '__all__'
        widgets = {
            'fecha_inicio' : widgets.DateInput(attrs={'type': 'date'}),
            'fecha_final' : widgets.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'