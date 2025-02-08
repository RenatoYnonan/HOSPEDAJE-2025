from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class CalendarioView(TemplateView):
    template_name = 'index-calendario.html'

class ReservasView(TemplateView):
    template_name = 'index-reservas.html'