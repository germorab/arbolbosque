# coding=utf-8
from rest_framework import viewsets
from rest_framework import filters

from bosque.models import Categoria, Articulo
from bosque.v1.serializers import CategoriaSerializer, ArticleSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nombre', )


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Articulo.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('titulo', )
