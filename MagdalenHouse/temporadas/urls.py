from django.urls import path
from . import views
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Temporada
from .forms import FormsTemporadas


urlpatterns = [
    path('', views.ListTemporada.as_view(), name='list-temporada'),
    path('nueva-temporada', views.CreateTemporada.as_view(), name='create-temporada'),
    path('edit-temporada/<int:pk>/', views.UpdateTemporada.as_view(), name='edit-temporada'),
    path('delete-temporada/<int:pk>/', views.DeleteTemporada, name='delete-temporada'),
]