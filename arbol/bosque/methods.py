from models import *

def consultarCategorias ():
    try:
        cats = Categoria.objects.all() 
    except:
        cats = []
    return cats


def guardarTextoNuevo (titulo, contenido, categoria):
    nt = Texto(titulo = titulo, contenido = contenido)
    nt.save()
    
    categoriai = Categoria.objects.get(id = categoria)
    
    ctl = CategoriaLink (categoria = categoriai, texto = nt)
    ctl.save()

def guardarCategoriaNueva (nombre, descripcion):
    nc = Categoria(nombre = nombre, descripcion = descripcion)
    nc.save()
