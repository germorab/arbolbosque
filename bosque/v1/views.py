# coding=utf-8
from rest_framework import viewsets
from rest_framework import filters

from bosque.models import Categoria, Articulo, Tematica
from bosque.v1.serializers import CategorySerializer, ArticleSerializer, ThematicSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Categoria.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nombre', )


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Articulo.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('titulo', )


class ThematicViewSet(viewsets.ModelViewSet):

    queryset = Tematica.objects.all()
    serializer_class = ThematicSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nombre', )
