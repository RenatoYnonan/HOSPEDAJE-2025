from django import forms
from ReserApp.models import ModelsReservas
from clientes.models import ModelsClientes


class CustomerForms(forms.ModelForm):
    class Meta:
        model = ModelsClientes
        fields = ['name_customer', 'last_name_customer', 'email_customer', 'phone_customer', 'address_customer', 'city_customer']
        widgets = {
            'name_customer' : forms.TextInput(attrs={'placeholder': 'Nombres', 'class': 'form-control'}),
            'last_name_customer' : forms.TextInput(attrs={'placeholder': 'Apellidos', 'class': 'form-control'}),
            'email_customer' : forms.EmailInput(attrs={'placeholder': 'Correo', 'class': 'form-control'}),
            'phone_customer' : forms.TextInput(attrs={'placeholder': 'Teléfono', 'class': 'form-control'}),
            'address_customer' : forms.TextInput(attrs={'placeholder': 'Dirección', 'class': 'form-control'}),
            'city_customer' : forms.TextInput(attrs={'placeholder': 'Ciudad', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ReservarForms(forms.ModelForm):
    class Meta:
        model = ModelsReservas
        fields = ['date_start', 'date_end', 'number_nights', 'number_people','price_total']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'