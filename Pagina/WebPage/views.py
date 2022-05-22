from django.shortcuts import render, redirect
from tienda.Carrito import Carrito
from tienda.models import Producto
import requests


# Create your views here.
def index(request):
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')


def blog(request):
    return render(request,'blog.html')

def productos(request):
    url = "http://127.0.0.1:8000/api/productos/"
    response = requests.get(url, auth = ('admin', '1234'))
    producto = response.json()
    return render(request,'product.html', context={'producto':producto})

def about(request):
    return render(request,'about.html')

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("/productos")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("/productos")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("/productos")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("/productos")

