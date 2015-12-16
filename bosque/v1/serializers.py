from rest_framework import serializers

from bosque.models import Categoria, Articulo, Tematica


class ThematicSerializer(serializers.ModelSerializer):

    categories_link = serializers.ReadOnlyField(
        source='get_categories_api_url'
    )

    class Meta:
        model = Tematica
        fields = ('nombre', 'descripcion', 'categories_link')


class CategorySerializer(serializers.ModelSerializer):

    articles_link = serializers.ReadOnlyField(
        source='get_articles_api_url'
    )

    class Meta:
        model = Categoria
        fields = ('nombre', 'descripcion', 'tematica', 'articles_link')
        depth = 1


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Articulo
        fields = ('titulo', 'contenido', 'categoria')
        depth = 2
