from django import forms
from django.forms import ModelForm
from .models import colaborador

class ColaboradorForm(ModelForm):

    class Meta:
        model = colaborador
        fields=['email', 'password', 'fotoP', 'rut', 'rutD', 'nombre', 'fono', 'direccion', 'pais', 'esAdmin', 'is_staff']