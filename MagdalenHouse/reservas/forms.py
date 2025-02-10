from  django.forms import ModelForm
from .models import *

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'