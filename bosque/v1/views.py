# coding=utf-8
from rest_framework import viewsets

from bosque.models import Categoria
from bosque.v1.serializers import CategoriaSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
