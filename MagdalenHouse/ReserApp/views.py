import datetime
from itertools import count
from webbrowser import get
from django import template
from django.db.models import query
from django.shortcuts import render, redirect
from django.views.generic import *
from .models import ModelsReservas

from clientes.forms import ClientesForm
from .forms import FormularioReserva
from django.urls import reverse_lazy
from django.http import JsonResponse
from datetime import date

from django.utils import timezone


from temporadas.models import *

#CALENDARIO
class CalendarioView(TemplateView):
    template_name = 'index-calendar.html'

  
def ObtenerReservas(request):
    reservas = ModelsReservas.objects.all()
    eventos = []
    
    for i in reservas:
        eventos.append({
            'id': i.pk,  # ID único de la reserva
            'title': i.customer_selection.name_customer, #Nombre del cliente
            'start': i.date_start.isoformat(), #Fecha de inicio donde reservo
            'end': i.date_end.isoformat() #Fecha de fin donde reservo
        })
    
    return JsonResponse(eventos, safe=False)


#RESERVAS
class ReservasView(View):
    template_name = 'index-reservas.html'

    #RENDERIZA LOS FORMULARIOS A LA PAGINA
    def get(self, request, *args, **kwargs):
        context = {
            'form': FormularioReserva(),
            'form_customer': ClientesForm(),
            'reservas': ModelsReservas.objects.order_by('-date_create_customer')[:3]
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form_type = request.POST.get("form_type")

        if form_type == "reservation":
            form = FormularioReserva(request.POST)
            if form.is_valid():
                start_date = form.cleaned_data['date_start']
                end_date = form.cleaned_data['date_end']
                departemento_id = form.cleaned_data['departamento_selection'].id

                # 📌 Verificar disponibilidad antes de guardar
                if not self.check_availability(start_date, end_date, departemento_id):
                    return JsonResponse({'available': False, 'message': 'Fechas no disponibles'}, status=400)

                form.save()
                return redirect('ReserApp:new-reserva')
            else:
                return JsonResponse({'available': False, 'message': 'Datos inválidos'}, status=400)

        elif form_type == "customer":
            form_customer = ClientesForm(request.POST)
            if form_customer.is_valid():
                form_customer.save()
                return redirect('ReserApp:new-reserva')

        context = {
            'form': FormularioReserva(),
            'form_customer': ClientesForm(),
        }
        return render(request, self.template_name, context)

    @staticmethod
    def check_availability(start_date, end_date, departamento_id):
        """
        Verifica si las fechas están disponibles. Retorna True si están disponibles, False si hay conflicto.
        """
        # 📌 Verificar si las fechas ya son tipo `date`, si no, convertirlas
        if isinstance(start_date, str):
            start_date = date.fromisoformat(start_date)

        if isinstance(end_date, str):
            end_date = date.fromisoformat(end_date)

        # 📌 Verificar si hay conflictos con reservas existentes
        conflicts = ModelsReservas.objects.filter(
            date_start__lte=end_date, 
            date_end__gte=start_date,
            departamento_selection_id=departamento_id,
        ).exists()

        # 📌 Verificar si hay una temporada disponible
        temporada_existente = Temporada.objects.filter(
            fecha_inicio__lte=start_date, fecha_final__gte=end_date
        ).exists()

        # 📌 Si hay conflicto o no hay temporada válida, retornar False
        return not conflicts and temporada_existente  

class ListReservas(ListView):
    model = ModelsReservas
    template_name = 'index-historial-reservas.html'
    context_object_name = 'reservar'

class DetailReservas(DetailView):
    model = ModelsReservas
    template_name = ''



class ReservaUpdate(UpdateView):
    model = ModelsReservas
    form_class =  FormularioReserva
    template_name = 'index-reservas-form.html'
    success_url = reverse_lazy('ReserApp:new-reserva')
