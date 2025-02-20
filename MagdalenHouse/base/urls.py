from django.urls import path
from . import views


urlpatterns = [
    path('', views.HospedajeView.as_view(), name='hospedaje-magdalen')
]