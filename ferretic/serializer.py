from rest_framework import serializers
from ferretic.models import *

class Ferretic_serializer(serializers.ModelSerializer):
    class Meta:
        model = Ferretic
        fields = '__all__'

class Proveedor_serializer(serializers.ModelSerializer):
    ferretic = Ferretic_serializer(read_only=True)
    ferretic_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Ferretic.objects.all(), source='ferretic')
    class Meta:
        model = Proveedor
        fields = '__all__'

class Categoria_serializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class Producto_serializer(serializers.ModelSerializer):
    proveedor = Proveedor_serializer(read_only=True)
    proveedor_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Proveedor.objects.all(), source='proveedor')
    categoria = Categoria_serializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Categoria.objects.all(), source='categoria')

    class Meta:
        model = Producto
        fields = '__all__'

class Pedido_serializer(serializers.ModelSerializer):
    producto = Producto_serializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(), source='producto')
    proveedor = Proveedor_serializer(read_only=True)
    proveedor_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Proveedor.objects.all(), source='proveedor')
    class Meta:
        model = Pedido
        fields = '__all__'

class Empleado_serializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'


class Cliente_serializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class Venta_serializer(serializers.ModelSerializer):
    producto = Producto_serializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(), source='producto')
    empleado = Empleado_serializer(read_only=True)
    empleado_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Empleado.objects.all(), source='empleado')
    class Meta:
        model = Venta
        fields = '__all__'