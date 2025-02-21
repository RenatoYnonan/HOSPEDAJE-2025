from django.shortcuts import render
from django.views.generic import *
from alojamiento.models import *

# Create your views here.
class HospedajeView(TemplateView):
    template_name = 'index-hospedaje.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['habitaciones'] = Habitaciones.objects.all()
        context['departamentos'] = Departamentos.objects.all()
        return context

class DetailAlojamiento(DetailView):
    model = Departamentos
    context_object_name = 'alojamiento'
    template_name = 'index-detail-habitacion.html'