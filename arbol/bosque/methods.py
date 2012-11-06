from models import *

def consultarCategorias ():
    try:
        cats = Categoria.objects.all() 
    except:
        cats = []
    return cats


def guardarTextoNuevo (titulo, contenido):
    nt = Texto(titulo = titulo, contenido = contenido)
    nt.save()
    #TODO guardar en categoriasLink  las categorias asociadas


def guardarCategoriaNueva (nombre, descripcion):
    nc = Categoria(nombre = nombre, descripcion = descripcion)
    nc.save()
