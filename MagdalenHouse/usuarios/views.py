from django.shortcuts import render
from django.views.generic import *

from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import EditUserForm, UsuarioForm, PasswordUserForm, GroupForm
from django.contrib.auth.views import PasswordChangeView

# Create your views here.

#USUARIOS
class UsuarioView(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'usuarios'
    template_name = 'index-usuario.html'

class CreateUserView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UsuarioForm
    template_name = 'index-usuario-form.html'
    success_url = reverse_lazy('usuarios:index-usuarios')

class EditUserView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditUserForm
    template_name = 'index-usuario-form.html'
    success_url = reverse_lazy('usuarios:index-usuarios')

class PasswordUserView(PasswordChangeView):
    form_class = PasswordUserForm
    template_name = 'index-usuario-form.html'
    success_url = reverse_lazy('usuarios:index-usuarios')

#GRUPOS
class GroupView(LoginRequiredMixin, ListView):
    model = Group
    context_object_name = 'groups'
    template_name = 'group/index-group.html'

class CreateGroupView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'group/index-group-form.html'
    success_url = reverse_lazy('usuarios:index-groups')