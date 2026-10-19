# catalogo/datos.py

LIBROS = [
    {"id": 1, "titulo": "El río de las palabras", "no_disponible": True},
    {"id": 2, "titulo": "Noches de lluvia", "no_disponible": True},
    {"id": 3, "titulo": "Python desde cero", "no_disponible": False},
    {"id": 4, "titulo": "El universo en tu bolsillo", "no_disponible": True},
    {"id": 5, "titulo": "Cuentos del Magdalena", "no_disponible": False},
    {"id": 6, "titulo": "Django paso a paso", "no_disponible": True},
]

def buscar_libro(libro_id):
    """Devuelve el libro con ese id, o None si no existe."""
    for libro in LIBROS:
        if libro["id"] == libro_id:
            return libro
    return None