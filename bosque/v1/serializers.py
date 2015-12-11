from rest_framework import serializers

from bosque.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nombre', 'descripcion')
