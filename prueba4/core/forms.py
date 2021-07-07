from django import forms
from django.forms import ModelForm
from .models import Mascotas

class MascotasForm(ModelForm):

    class Meta:
        model = Mascotas
        fields=['raza', 'edad', 'nombre', 'chip']