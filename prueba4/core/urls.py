from django.urls import path
from .views import home, formulario1, formulario2, formulario3, verdatos

urlpatterns=[
    path('', home, name="home"),
    path('Agregar-objetos', formulario1, name="Form1"),
    path('Mod-datos/<id>', formulario2, name="Form2"),
    path('Elim-datos/<id>', formulario3, name="Form3"),
    path('Ver-datos', verdatos, name="VerD"),
]