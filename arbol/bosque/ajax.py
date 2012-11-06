from methods import *
from dajax.core import Dajax
from django.utils import simplejson
from dajaxice.core import dajaxice_functions
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string

@dajaxice_register
def guardarTexto (request, titulo, contenido):
    dajax = Dajax()
    
    guardarTextoNuevo(titulo, contenido)
    
    dajax.assign('#resultado','innerHTML',"Contenido ingresado")
    return dajax.json()

@dajaxice_register
def guardarCategoria (request, nombre, descripcion):
    dajax = Dajax()
    
    guardarCategoriaNueva(nombre, descripcion)
    
    dajax.assign('#resultado','innerHTML',"Categoria creada")
    return dajax.json()
