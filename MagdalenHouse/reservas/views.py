from webbrowser import get
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from .models import Reserva
from .forms import ReservaForm
from clientes.forms import ClientesForm
from django.urls import reverse_lazy
from django.http import JsonResponse

# Create your views here.
class CalendarioView(TemplateView):
    template_name = 'index-calendario.html'

class ReservasView(CreateView):
    form_class = ReservaForm
    template_name = 'index-reservas.html'
    success_url = reverse_lazy('reservas:index-calendar')

            
    
