from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import *
from django.urls import reverse_lazy
from django.http  import JsonResponse
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




# DEPARTAMENTOS
class DepartamentosView(ListView):
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



def DeleteDepartament(request,id):
    dp = get_object_or_404(Departamentos, id=id)
    if request.method == 'POST':
        if dp.active_booking:
            dp.active_booking = False
            dp.save()
            return redirect('alojamiento:index-departamento')
        else:
            return JsonResponse({'error': 'El usuario ya está inactivo'})
    return render(request, 'departamentos/index-departamentos-forms.html')