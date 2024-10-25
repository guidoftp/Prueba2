from django.db import models

# Create your models here.

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    fecha_lanz = models.DateField()
    desarrolladora = models.CharField(max_length=50)
    precio = models.FloatField()