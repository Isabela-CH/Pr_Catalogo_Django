# config/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("App_Catalogo.urls")),  # Incluye las rutas de la app en la raíz del sitio
]