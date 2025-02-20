from django.shortcuts import render
from django.views.generic import *

# Create your views here.
class HospedajeView(TemplateView):
    template_name = 'index-hospedaje.html'