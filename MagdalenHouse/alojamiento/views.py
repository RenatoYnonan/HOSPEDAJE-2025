from django.shortcuts import render, redirect ,get_object_or_404
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

# HABITACIONES
class Habitaciones(ListView):
    model = Habitaciones
    context_object_name = 'obj_alojamiento'
    template_name = 'habitaciones/index-habitaciones.html'

class CreateHabitaciones(CreateView):
    model  = Habitaciones
    form_class  = HabitacionesForm
    template_name = 'habitaciones/index-habitaciones-forms.html'
    success_url = reverse_lazy('alojamiento:index-habitacion')

class UpdateHabitaciones(UpdateView):
    model  = Habitaciones
    form_class  = HabitacionesForm
    template_name = 'habitaciones/index-habitaciones-forms.html'
    success_url = reverse_lazy('alojamiento:index-habitacion')

def DeleteHabitaciones(request, id):
    habitacion = get_object_or_404(id=id)
    if request.method == 'POST':
        if habitacion.active_booking is  True:
            habitacion.active_booking = False
            habitacion.save()
            return redirect('alojamiento:index-habitacion')
    return render(request, 'habitaciones/index-habitaciones-forms.html')



# DEPARTAMENTOS
class Departamentos(ListView):
    model = Departamentos
    context_object_name = 'obj_alojamiento'
    template_name = 'departamentos/index-departamentos.html'

class CreateDepartamentos(CreateView):
    model  = Departamentos
    form_class  = DepartamentosForm
    template_name = 'departamentos/index-departamentos-forms.html'
    success_url = reverse_lazy('alojamiento:index-departamento')

class UpdateDepartamentos(UpdateView):
    model  = Departamentos
    form_class  = DepartamentosForm
    template_name = 'departamentos/index-departamentos-forms.html'
    success_url = reverse_lazy('alojamiento:index-departamento')

def DeleteDepartamentos(request, id):
    departamento = get_object_or_404(id=id)
    if request.method == 'POST':
        if departamento.active_booking is  True:
            departamento.active_booking = False
            departamento.save() 
            return redirect('alojamiento:index-departamento')
    return render(request, 'departamentos/index-departamentos-forms.html')