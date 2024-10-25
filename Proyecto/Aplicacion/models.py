from django.core.validators import MinValueValidator
from django.db import models
# Create your models here.

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    fecha_lanz = models.DateField()
    desarrolladora = models.CharField(max_length=100)
    precio = models.FloatField(validators=[MinValueValidator(0)])
