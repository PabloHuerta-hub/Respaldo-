from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login

import requests

# Create your views here.
from producto.models import Producto
from producto.Carrito import Carrito

def index(request):
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')


def blog(request):
    return render(request,'blog.html')

def contador(request):
    return render(request,'contador.html')

def bodeguero(request):
    return render(request,'bodeguero.html')

def vendedor(request):
    return render(request,'vendedor.html')

def registrarse(request):
    return render(request,'register.html')

def product(request):
    url = 'http://127.0.0.1:8000/api/productos/' 
    response = requests.get(url, auth = ('admin', '1234'))
    data = response.json()
    productos = {'productos': data}
    return render(request,'product.html', productos)

def carrito(request):
    url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(url, auth = ('admin', '1234'))
    data = response.json()
    productos = {'productos': data}
    return render(request,'carrito.html', productos)


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Product")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def sumar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.sumar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")
