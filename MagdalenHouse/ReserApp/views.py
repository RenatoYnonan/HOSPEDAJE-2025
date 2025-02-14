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

# Create your views here.

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

    def get(self, request, *args, **kwargs):
        query =  request.GET.get('search')
        if query:
            reservas = ModelsReservas.objects.filter(customer_selection__name_customer__icontains=query)

        else:
            reservas = ModelsReservas.objects.all()

        context = {
            'form': FormularioReserva(),
            'form_customer': ClientesForm(),
            'reservas' :  reservas
        }
        print(query)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form_type = request.POST.get("form_type")

        if form_type == "reservation":
            form = FormularioReserva(request.POST)
            if form.is_valid():
                form.save()
                return redirect('ReserApp:new-reserva')
            else:
                return JsonResponse(form.errors.as_json(), safe=False)

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
    

    
class ReservaUpdate(UpdateView):
    model = ModelsReservas
    form_class =  FormularioReserva
    template_name = 'index-reservas-form.html'
    success_url = reverse_lazy('ReserApp:new-reserva')
