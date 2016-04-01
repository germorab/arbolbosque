# coding=utf-8
from rest_framework import serializers

from bosque.models import Categoria, Articulo, Tematica


class ArticleSerializer(serializers.ModelSerializer):

    categories_link = serializers.ReadOnlyField(
        source='get_categories_api_url'
    )

    class Meta:
        model = Articulo
        fields = ('id', 'titulo', 'contenido', 'categories_link')


class CategorySerializer(serializers.ModelSerializer):

    thematic_link = serializers.ReadOnlyField(
        source='get_thematic_api_url'
    )

    class Meta:
        model = Categoria
        fields = ('id', 'nombre', 'descripcion', 'thematic_link')


class ThematicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tematica
        fields = ('id', 'nombre', 'descripcion')
