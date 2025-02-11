from tabnanny import verbose
from django.db import models

# Create your models here.
class ModelsClientes(models.Model):
    name_customer = models.CharField(max_length=100, verbose_name='Nombre Completo')
    last_name_customer = models.CharField(max_length=100, verbose_name='Apellido')
    email_customer = models.EmailField(max_length=100, unique=True, verbose_name='Email')
    phone_customer = models.CharField(max_length=100, verbose_name='Telefono')
    address_customer = models.CharField(max_length=100, verbose_name='Direccion')
    city_customer = models.CharField(max_length=100, verbose_name='Ciudad')
    active_customer = models.BooleanField(verbose_name='Estado', default=True)
    date_create_customer = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')

    def __str__(self):
        return f"{self.name_customer} {self.last_name_customer}"
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'clientes'
