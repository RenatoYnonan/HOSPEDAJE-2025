from django.shortcuts import render
from django.views.generic import ListView

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class UsuarioView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'usuario_list.html'