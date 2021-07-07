from django.shortcuts import render, redirect
from .models import Mascotas
from .forms MascotasForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def formulario1(request):
    return render(request, 'core/formulario1.html')

def formulario2(request, id):

    mascotas = Mascotas.objects.get(raza=id)

    datos = {
        'mascotas': MascotasForm(instance=mascotas)
    }

if request.method== 'POST':

    formulario = MascotasForm(data=request.POST, instance=mascotas)

    if formulario.is.valid:

        formulario.save()

        datos ['mensaje'] = "Modificados Correctamente"

    return render(request, 'core/formulario2.html', datos)

def formulario3(request, id):

    mascotas = Mascotas.objects.get(raza=id)

    mascotas.delete()

    return redirect(to="VerD")

def verdatos(request):
    mascotas=Mascotas.objects.all()

    datos = {
        'mascotas': mascotas
    }
    return render(request, 'core/verdatos.html', datos)