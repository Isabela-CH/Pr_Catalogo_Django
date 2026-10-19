# catalogo/urls.py
from django.urls import path
from . import views

app_name = "App_Catalogo"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("libros/", views.lista_libros, name="lista_libros"),
    path("libros/no-disponibles/", views.libros_no_disponibles, name="no_disponibles"), # Ejercicio Isabella
    path("libros/<int:libro_id>/", views.detalle_libro, name="detalle_libro"),
    path("acerca/", views.AcercaView.as_view(), name="acerca"),
]