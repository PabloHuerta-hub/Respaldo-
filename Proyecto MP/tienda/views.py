from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import requests
from tienda.forms import RegistroUsuarios
from django.contrib.auth.models import Group
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

#Registro de clientes los usuarios staff deben ser creados manualmente y se les debe asignar un rol 
def registrarse(request):
    context={}
    if request.POST:
        form=RegistroUsuarios(request.POST)
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
        form=RegistroUsuarios()
        context['registro']=form
    return render(request,'register.html',context)


def loginPage(request):
    if request.method == "POST":
        #se reciben los datos del formulario
        username = request.POST.get("username")
        password = request.POST.get("password")
        #se autentica al usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Index')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request,'login.html', context)

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
