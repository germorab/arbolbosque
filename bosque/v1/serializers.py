from rest_framework import serializers

from bosque.models import Categoria, Articulo, Tematica


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nombre', 'descripcion')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('titulo', 'contenido')


class ThematicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tematica
        fields = ('nombre', 'descripcion')
