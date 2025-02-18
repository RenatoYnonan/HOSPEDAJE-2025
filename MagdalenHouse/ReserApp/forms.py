from django import forms
from .models import ModelsReservas
from clientes.models import ModelsClientes


class FormularioReserva(forms.ModelForm):
    class Meta:
        model = ModelsReservas
        fields = '__all__'
        widgets = {
            'date_start' : forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_end' : forms.DateInput(attrs={'type': 'date'}),
            'number_nights' : forms.NumberInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_selection'].queryset = ModelsClientes.objects.filter(active_customer=True)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

            if field_name == 'customer_selection':
                field.widget.attrs['class'] = 'js-example-basic-single form-control'