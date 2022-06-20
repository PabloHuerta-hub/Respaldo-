from django.shortcuts import render
from rest_framework import viewsets, permissions
from producto.models import Producto, Direccion, Cliente
from MusicPro.appApi.serializers import  DireccionSerializer, ClienteSerializer
from MusicPro.appApi import serializers
# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = serializers.ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    permissions = [permissions.IsAuthenticated]


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permissions = [permissions.IsAuthenticated]
