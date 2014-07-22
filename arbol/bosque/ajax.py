from methods import *
from dajax.core import Dajax
from django.utils import simplejson
from dajaxice.core import dajaxice_functions
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
#from django.views.decorators.csrf import csrf_ensure_cookie


@dajaxice_register
def guardarTexto (request, titulo, contenido, categoria):
    dajax = Dajax()
    
    try :
        guardarTextoNuevo(titulo, contenido, categoria)
    except:
        dajax.script("arbolfunctions.texto.setResultadoError();")
        
    dajax.script("arbolfunctions.texto.setResultadoOK();")
    
    return dajax.json()

@dajaxice_register
def guardarCategoria (request, nombre, descripcion):
    dajax = Dajax()
    
    guardarCategoriaNueva(nombre, descripcion)
    dajax.script("arbolfunctions.categoria.setResultadoOK();")
    
    return dajax.json()


@dajaxice_register
def mostrarDialogoCategoria (request):
    dajax = Dajax()
    
    outvars = []
    dajax.assign('#dialog-confirm','innerHTML',render_to_string('crearcategoria.html'))
    dajax.add_data(outvars,"arbolfunctions.indice.diag")

    return dajax.json()

@dajaxice_register
def mostrarDialogoTexto (request):
    dajax = Dajax()
    
    categorias = consultarCategorias()
    outvars = []
    dajax.assign('#dialog-confirm','innerHTML',render_to_string('creartexto.html', {'categorias':categorias}))
    dajax.add_data(outvars,"arbolfunctions.indice.diag")

    return dajax.json()


@dajaxice_register
def mostrarDialogoBusqueda (request):
    dajax = Dajax()
    
    outvars = []
    dajax.assign('#dialog-confirm','innerHTML',render_to_string('busqueda.html'))
    dajax.add_data(outvars,"arbolfunctions.indice.diag")

    return dajax.json()


@dajaxice_register
def mostrarDialogoImagen (request):
    dajax = Dajax()
    
    outvars = []
    dajax.assign('#dialog-confirm','innerHTML',render_to_string('cargarimagen.html'))
    dajax.add_data(outvars,"arbolfunctions.indice.diag")

    return dajax.json()


@dajaxice_register
def mostrarDialogoPagina (request):
    dajax = Dajax()
    
    consultarPagina("test")
    
    outvars = []
    dajax.assign('#dialog-confirm','innerHTML',render_to_string('pagina.html'))
    dajax.add_data(outvars,"arbolfunctions.indice.diag")

    return dajax.json()
