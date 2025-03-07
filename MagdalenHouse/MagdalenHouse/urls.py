"""
URL configuration for MagdalenHouse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('base.urls', 'base'), namespace='base')),
    path('magdalen_intranet/', include(('magdalen_intranet.urls', 'magdalen_intranet'), namespace='magdalen_intranet')),
    path('usuarios/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
    path('clientes/', include(('clientes.urls', 'clientes'), namespace='clientes')),
    path('mdreser/', include(('ReserApp.urls', 'ReserApp'), namespace='ReserApp')),
    path('alojamiento/', include(('alojamiento.urls', 'alojamiento'), namespace='alojamiento')),
    path('temporadas/', include(('temporadas.urls', 'temporadas'), namespace='temporadas')),
]


