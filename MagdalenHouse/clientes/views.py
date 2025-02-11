from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.views.generic import *
from django.urls import reverse_lazy
from .forms import ClientesForm
from django.contrib.auth.mixins import LoginRequiredMixin
        
# Create your views here.

class ClientesView(LoginRequiredMixin, TemplateView):   
    template_name = 'index-clientes.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['clientes'] = ModelsClientes.objects.all()
        context['form'] = ClientesForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ClientesForm(self.request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:index-clientes')
        else:
            context = self.get_context_data()
            context['form'] = form
            return render(request, self.template_name, context)