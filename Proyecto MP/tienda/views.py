from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import requests
from tienda.forms import RegistroUsuarios,Clientes
from django.contrib.auth.models import Group
# Create your views here.
from producto.models import Producto
from producto.Carrito import Carrito

def index(request):
    return render(request,'Inicio/index.html')


def contact(request):
    return render(request,'Inicio/contact.html')


def blog(request):
    return render(request,'Inicio/blog.html')
#Vista contador
def entregascontador(request):
    if request.user.is_authenticated:
        for group in request.user.groups.all():
            if group.name == 'Contador':
                return render(request,'Contador/entregascontador.html')
            else:
                return redirect('login')
    else:
        return redirect('Index')
def pagoscontador(request):
    if request.user.is_authenticated:
        for group in request.user.groups.all():
            if group.name == 'Contador':
                return render(request,'Contador/pagoscontador.html')
            else:
                return redirect('login')
    else:
        return redirect('Index')
#Vista bodeguero
def productobodeguero(request): 
    if request.user.is_authenticated:
        for group in request.user.groups.all():
            if group.name == 'Bodeguero':
                return render(request,'Bodeguero/productosbodeguero.html')
            else:
                return redirect('login')
    else:
        return redirect('Index')
    
def ordenesbodeguero(request):
    if request.user.is_authenticated:
        for group in request.user.groups.all():
            if group.name == 'Bodeguero':
                return render(request,'Bodeguero/ordenesbodeguero.html')
            else:
                return redirect('login')
    else:
        return redirect('Index') 
#Vista vendedor
def productovendedor(request):
    if request.user.is_authenticated:
        for group in request.user.groups.all():
            if group.name == 'Vendedor':
                return render(request,'Vendedor/productosvendedor.html')
            else:
                return redirect('login')
    else:
        return redirect('Index')

def pedidosvendedor(request):
    if request.user.is_authenticated:
        for group in request.user.groups.all():
            if group.name == 'Vendedor':
                return render(request,'Vendedor/pedidosvendedor.html')
            else:
                return redirect('login')
    else:
        return redirect('Index')
    
def ordenesvendedor(request):
    if request.user.is_authenticated:
        for group in request.user.groups.all():
            if group.name == 'Vendedor':
                return render(request,'Vendedor/ordenesvendedor.html')
            else:
                return redirect('login')
    else:
        return redirect('Index')
#Registro de clientes los usuarios staff deben ser creados manualmente y se les debe asignar un rol 
def registrarse(request):
    context={}
    if request.POST:
        form=Clientes(request.POST)
        #se valida el formulario
        if form.is_valid():
            user= form.save(commit=False)
            user.save()
            #se ingresa el usuario automaticamente al grupo cliente
            group = Group.objects.get(name='Cliente')
            user.groups.add(group)
            #se redigire al index
            return redirect('Index')
        else:
            #si el formulario no es valido se muestra el formulario de nuevo
            context['registro']=form
    else:
        #en caso que no ha metodo post se muestra el formulario
        form=Clientes()
        context['registro']=form
    return render(request,'Inicio/register.html',context)



def product(request):
    url = 'http://127.0.0.1:8000/api/productos/' 
    response = requests.get(url, auth = ('admin@gmail.com', '123'))
    data = response.json()
    productos = {'productos': data}
    return render(request,'Inicio/product.html', productos)

def carrito(request):
    url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(url, auth = ('admin@gmail.com', '1234'))
    data = response.json()
    productos = {'productos': data}
    return render(request,'Inicio/carrito.html', productos)


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
