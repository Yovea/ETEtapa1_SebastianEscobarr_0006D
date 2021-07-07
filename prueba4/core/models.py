from django.db import models

# Create your models here.

class Mascotas(models.Model):
    raza = models.CharField(max_length=20, primary_key=True, verbose_name='Raza')
    edad = models.CharField(max_length=2, verbose_name='Edad')
    nombre = models.CharField(max_length=25, verbose_name='Nombre')
    chip = models.CharField(max_length=2, verbose_name='Chip')
    
    def __str__(self):
        return self.nombre