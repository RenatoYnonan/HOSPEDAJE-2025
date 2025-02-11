from django.shortcuts import render, redirect, get_object_or_404
from .models import *

from django.views.generic import *
from django.urls import reverse_lazy
from .forms import ClientesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView

# Create your views here.

class ClientesView(LoginRequiredMixin, ListView):
    model = ModelsClientes
    context_object_name = 'clientes'
    template_name = 'index-clientes.html'


class CreateClientes(LoginRequiredMixin, CreateView):
    model = ModelsClientes
    form_class = ClientesForm
    template_name = 'index-clientes-form.html'
    success_url = reverse_lazy('clientes:index-clientes')


class UpdateClientes(LoginRequiredMixin, UpdateView):
    model = ModelsClientes
    form_class = ClientesForm
    template_name = 'index-clientes-form.html'
    success_url = reverse_lazy('clientes:index-clientes')