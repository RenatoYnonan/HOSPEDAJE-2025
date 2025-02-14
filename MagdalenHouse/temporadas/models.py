from django.db import models
from alojamiento.models import Departamentos

# Create your models here.
class Temporada(models.Model):
    nombre_temporada = models.CharField(max_length=250, default='Temporada sin nombre')
    alojamiento = models.ManyToManyField(Departamentos, related_name='alojamiento')
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Temporada'
        verbose_name_plural = 'Temporadas'
        db_table = 'Temporadas'

    def __str__(self):
        return f"{self.nombre_temporada} ({self.fecha_inicio} - {self.fecha_final})"