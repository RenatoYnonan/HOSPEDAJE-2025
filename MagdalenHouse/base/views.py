from this import d
from django.shortcuts import render
from datetime import datetime
from django.views.generic import *
from alojamiento.models import *
from ReserApp.models import *

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
