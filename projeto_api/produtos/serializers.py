from rest_framework import serializers
from .models import Categoria, Produto

class CategoriaSerializers (serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
class ProdutoSerializer (serializers.ModelSerializer):
    categoria = CategoriaSerializer (read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects,source='categoria', write_only=True)
    class Meta:
        Model = Produto
        fields = '__all__'