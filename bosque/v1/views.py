# coding=utf-8
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import generics

from bosque.models import Categoria, Articulo, Tematica
from bosque.v1.serializers import CategorySerializer, ArticleSerializer, ThematicSerializer


class ThematicViewSet(viewsets.ModelViewSet):

    queryset = Tematica.objects.all()
    serializer_class = ThematicSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nombre', )


class ThematicCategories(generics.ListAPIView):

    model = Categoria
    serializer_class = CategorySerializer

    def get_queryset(self):

        thematic_pk = self.kwargs.get('pk')

        queryset = Categoria.objects.filter(tematica__pk=thematic_pk)

        return queryset


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Categoria.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nombre', )


class CategoryArticles(generics.ListAPIView):

    model = Articulo
    serializer_class = ArticleSerializer

    def get_queryset(self):

        category_pk = self.kwargs.get('pk')

        queryset = Articulo.objects.filter(categoria__pk=category_pk)

        return queryset


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Articulo.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('titulo', )

