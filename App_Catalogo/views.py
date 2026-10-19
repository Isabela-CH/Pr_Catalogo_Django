# catalogo/views.py
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from .datos import LIBROS, buscar_libro

def inicio(request):
    contexto = {"nombre_sitio": "Catálogo ADSO", "total": len(LIBROS)}
    return render(request, "App_Catalogo/inicio.html", contexto)

def lista_libros(request):
    genero = request.GET.get("genero", "")
    if genero:
        libros = [libro for libro in LIBROS if libro["genero"] == genero]
    else:
        libros = LIBROS
    return render(request, "App_Catalogo/lista.html", {"libros": libros , "genero": genero, "total": len(libros)})
def libros_no_disponibles(request):
    # Filtramos en la vista para mantener limpia la plantilla (Separación de responsabilidades)
    libros = [libro for libro in LIBROS if libro["no_disponible"] == True]
    contexto = {
        "libros": libros,
        "total": len(libros)
    }
    return render(request, "App_Catalogo/no_disponibles.html", contexto)

def detalle_libro(request, libro_id):
    libro = buscar_libro(libro_id)
    if libro is None:
        raise Http404("El libro no existe")
    return render(request, "App_Catalogo/detalle.html", {"libro": libro})

class AcercaView(TemplateView):
    template_name = "App_Catalogo/acerca.html"
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["version"] = "1.0"
        return contexto