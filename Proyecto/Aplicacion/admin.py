from django.contrib import admin
from Aplicacion.models import Juego

class JuegoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'fecha_lanz', 'desarrolladora', 'precio']
# Register your models here.
admin.site.register(Juego)

