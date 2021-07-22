from django.shortcuts import render, redirect
from .models import colaborador
from .forms ColaboradorForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def formulario1(request):
    return render(request, 'core/formulario1.html')

def formulario2(request, id):

    colaborador = colaborador.objects.get(raza=id)

    datos = {
        'colaborador': ColaboradorForm(instance=colaborador)
    }

if request.method== 'POST':

    formulario = ColaboradorForm(data=request.POST, instance=colaborador)

    if formulario.is.valid:

        formulario.save()

        datos ['mensaje'] = "Modificados Correctamente"

    return render(request, 'core/formulario2.html', datos)

def formulario3(request, id):

    colaborador = colaborador.objects.get(raza=id)

    colaborador.delete()

    return redirect(to="VerD")

def verdatos(request):
    colaborador=colaborador.objects.all()

    datos = {
        'colaborador': colaborador
    }
    return render(request, 'core/verdatos.html', datos)