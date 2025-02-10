from django.forms import ModelForm
from .models import *

class HabitacionesForm(ModelForm):
    class Meta:
        model = Habitaciones
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_a, field_b in self.fields.items():
            field_b.widget.attrs['class'] = 'form-control'



class DepartamentosForm(ModelForm):
    class Meta:
        model = Departamentos
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_a, field_b in self.fields.items():
            field_b.widget.attrs['class'] = 'form-control'
        