# coding=utf-8
from rest_framework import viewsets

from bosque.models import Categoria, Articulo
from bosque.v1.serializers import CategoriaSerializer, ArticleSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Articulo.objects.all()
    serializer_class = ArticleSerializer
