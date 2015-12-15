from rest_framework import serializers

from bosque.models import Categoria, Articulo


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nombre', 'descripcion')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('titulo', 'contenido')
