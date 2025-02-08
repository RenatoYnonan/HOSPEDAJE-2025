from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.urls import reverse_lazy
from .forms import ClientesForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ClientesView(LoginRequiredMixin, ListView):
    model = ModelsClientes
    context_object_name = 'clientes'
    template_name = 'index-clientes.html'


class CreateClientesView(LoginRequiredMixin, CreateView):
    model = ModelsClientes
    form_class = ClientesForm
    template_name = 'index-clientes-form.html'
    success_url = reverse_lazy('clientes:index-clientes')