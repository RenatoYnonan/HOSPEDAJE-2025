from this import d
from typing import Self
from django.shortcuts import render, redirect
from datetime import datetime
from django.views.generic import *
from clientes.forms import ClientesForm
from alojamiento.models import *
from ReserApp.models import *
from .forms import *
from clientes.models import *
from datetime import timedelta
from django.db import transaction
import json
from django.core.serializers.json import DjangoJSONEncoder

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        departamento = self.object

        # Filtrar reservas para este departamento
        reservas = ModelsReservas.objects.filter(departamento_selection=departamento)

        # Generar un rango de fechas ocupadas
        dias_ocupados = []
        for reserva in reservas:
            dias_ocupados.extend(
                [reserva.date_start + timedelta(days=i) 
                 for i in range((reserva.date_end - reserva.date_start).days + 1)]
            )

        # Pasar los días ocupados al contexto
        context['dias_ocupados_json'] = json.dumps(dias_ocupados, cls=DjangoJSONEncoder)
        return context




def habitaciones_disponibles(request):
    error = None
    departamentos_disponibles = Departamentos.objects.all()

    # Verificar que se hayan enviado las fechas por GET
    if "Check-entrada" in request.GET and "Check-salida" in request.GET:
        check_in = request.GET.get("Check-entrada")          
        check_out = request.GET.get("Check-salida")

        try:
            # Convertir las cadenas a objetos date
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()

            if check_in_date >= check_out_date:
                error = "La fecha de check-in debe ser anterior a la de check-out."
            else:
                # Excluir habitaciones con reservas que se solapen con el rango solicitado
                departamentos_disponibles = Departamentos.objects.exclude(
                    Departamento__date_start__lt=check_out_date,
                    Departamento__date_end__gt=check_in_date
                )

        except ValueError:
            error = "Formato de fecha incorrecto. Use AAAA-MM-DD."

    context = {
        "departamentos": departamentos_disponibles,
        "error": error,
    }

    return render(request, "index-resultados.html", context)


class Gracias(TemplateView):
    template_name = 'index-gracias.html'


def crear_reserva(request):
    fecha_en = request.GET.get('checkin', '')
    fecha_sal = request.GET.get('checkout', '')
    precio_ng =  request.GET.get('price', '')

    if request.method == "POST":
        cliente_form = CustomerForms(request.POST)
        reserva_form = ReservarForms(request.POST)
        if cliente_form.is_valid() and reserva_form.is_valid():
            with transaction.atomic():
                # Guarda los datos del cliente
                cliente = cliente_form.save()
                # Asigna el cliente a la reserva sin guardarla aún
                reserva = reserva_form.save(commit=False)
                reserva.customer_selection = cliente
                reserva.save()
            return redirect('base:gracias')  # Redirecciona según tu lógica
    else:
        cliente_form = CustomerForms()
        reserva_form = ReservarForms()

    context = {
        'cliente_form': cliente_form,
        'reserva_form': reserva_form,
        'fecha_en': fecha_en,
        'fecha_sal': fecha_sal,
        'precio_ng': precio_ng,
    }
    return render(request, "index-reservas-add.html", context)