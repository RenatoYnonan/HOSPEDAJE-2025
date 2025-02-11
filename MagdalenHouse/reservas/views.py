from webbrowser import get
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, View
from .models import Reserva
from .forms import ReservaForm
from clientes.forms import ClientesForm
from django.urls import reverse_lazy
from django.http import JsonResponse

# Create your views here.
class CalendarioView(TemplateView):
    template_name = 'index-calendario.html'

class ReservasView(View):
    template_name = 'index-reservas.html'

    def get(self, request, *args, **kwargs):
        context = {
            'form': ReservaForm(),
            'form_customer': ClientesForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form_type = request.POST.get("form_type")

        if form_type == "reservation":
            form = ReservaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('reservas:new-reserva')

        elif form_type == "customer":
            form_customer = ClientesForm(request.POST)
            if form_customer.is_valid():
                form_customer.save()
                return redirect('reservas:new-reserva')

        context = {
            'form': ReservaForm(),
            'form_customer': ClientesForm(),
        }
        return render(request, self.template_name, context)
    
