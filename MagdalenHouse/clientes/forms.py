from django.forms import ModelForm
from .models import ModelsClientes

class ClientesForm(ModelForm):
    class Meta:
        model = ModelsClientes
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'