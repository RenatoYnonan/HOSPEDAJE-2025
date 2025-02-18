from django.shortcuts import redirect, render
from .models import Temporada
from django.views.generic  import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import FormsTemporadas
from django.urls import reverse_lazy

# Create your views here.

class ListTemporada(ListView):
    model = Temporada
    template_name = 'index-temporadas.html'
    context_object_name = 'temporadas'


class CreateTemporada(CreateView):
    model = Temporada
    form_class = FormsTemporadas
    template_name = 'index-temporadas-form.html'
    success_url = reverse_lazy('temporadas:list-temporada')

class UpdateTemporada(UpdateView):
    model = Temporada
    form_class = FormsTemporadas
    template_name = 'index-temporadas-form.html'
    success_url = reverse_lazy('temporadas:list-temporada')

def DeleteTemporada(request, pk):
    if request.method == 'POST':
        temporada = Temporada.objects.get(pk=pk)
        if temporada.estado:
            temporada.estado = False
            temporada.save()
            return redirect('temporadas:list-temporada')
        else:
            temporada.estado = True
            temporada.save()
            return redirect('temporadas:list-temporada')
    return render(request, 'index-temporadas-form.html')
