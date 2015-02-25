from methods import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer



@ensure_csrf_cookie
def mostrarArbol(request):
    return render_to_response('arbol.html')


@ensure_csrf_cookie
def crearTexto(request):
    
    cats = consultarCategorias()

    listadecats = []
    for i in cats:
        listadecats.append([i.id,i.nombre])
    
    c = {'categorias' : listadecats}
    return render_to_response('creartexto.html', c, context_instance=RequestContext(request))

@ensure_csrf_cookie
def crearCategoria(request):
    return render_to_response('crearcategoria.html')



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
