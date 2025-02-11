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

class ReservasView(TemplateView):
    template_name = 'index-reservas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] =  ReservaForm()
        context['form_customer'] =  ClientesForm
        return context
    
    def post(self, request, *args, **kwargs):
        form = ClientesForm(self.request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas:new-reserva')
        else:
            context = self.get_context_data()
            context['form_customer'] = form
            return render(request, self.template_name, context)
