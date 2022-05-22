# serializers.py
# Aqui vamos a definir que campos vamos a mostrar
# para cada modelo.
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tienda.models import Producto
        
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
        fields = ['nombre', 'codigo', 'precio', 'serie_producto', 'marca', 'imagen','categoria']