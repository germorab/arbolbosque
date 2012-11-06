from methods import *
from django.template import RequestContext
from django.shortcuts import render_to_response


def crearTexto(request):
    
    cats = consultarCategorias()

    listadecats = []
    for i in cats:
        listadecats.append(i.nombre)
        
    c = {'categorias' : listadecats}
    return render_to_response('creartexto.html', c, context_instance=RequestContext(request))


def crearCategoria(request):
    return render_to_response('crearcategoria.html')
