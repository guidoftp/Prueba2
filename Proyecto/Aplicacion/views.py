from django.shortcuts import render,redirect
from Aplicacion.forms import FormJuego
from Aplicacion.models import Juego

# Create your views here.

def index(request):
    return render(request,'Aplicacion/index.html')

def listadoJuegos(request):
    juegos = Juego.objects.all()
    data = {'juegos' : juegos}
    return render(request, 'Aplicacion/juegos.html',data)

def agregarJuego(request):
    form = FormJuego()
    if request.method == 'POST':
        form = FormJuego(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'Aplicacion/agregarJuego.html',data)

def eliminarJuego(request, id):
    juego = Juego.objects.get(id = id)
    juego.delete()
    return redirect('/juegos/')

def actualizarJuego(request, id):
    juego = Juego.objects.get(id = id)
    form = FormJuego(instance=juego)
    if request.method == 'POST':
        form = FormJuego(request.POST, instance=juego)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render (request, 'Aplicacion/agregarJuego.html',data)


