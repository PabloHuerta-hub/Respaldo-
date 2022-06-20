from django.contrib.auth.models import User, Group
from rest_framework import serializers
from producto.models import Producto, Cliente, Direccion
        
class UserSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProductoSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Producto
        fields = ['url', 'id', 'nombre', 'codigo', 'precio', 'serie_producto', 'marca', 'imagen','categoria']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['url', 'serieCliente', 'nombre', 'rut', 'correo',
                  'id_usuario', 'direccion']

class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        fields = ['url', 'idDireccion', 'calle', 'numero', 'comuna',
                  'region', 'depto']