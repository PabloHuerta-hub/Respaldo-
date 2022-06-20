"""MusicPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from MusicPro.appApi import views
from django.conf.urls.static import static
from tienda.views import product,index,contact,blog,carrito,  agregar_producto, eliminar_producto,sumar_producto, limpiar_carrito, restar_producto,contador,bodeguero,vendedor,registrarse
router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
router.register(r'productos', views.ProductoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),#Autentificación de la API
    path('',index, name='Index'),
    path('contactanos',contact, name='Contactanos'),
    path('blog',blog,name='Blog'),
    path('productos',product,name='Product'),
    path('carrito',carrito,name='carrito'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('sumar/<int:producto_id>/', sumar_producto,name="Sum"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('contador', contador, name="Contador"),
    path('vendedor',vendedor,name="Vendedor"),
    path('bodeguero',bodeguero,name="bodeguero"),
    path('registrarse',registrarse,name="Registrarse"),
    #Se usa auth de django para mantener un usuario de la base de datos autenticado falta recibir el grupo de estos usuarios para dividir los templates por grupo
    path('login',LoginView.as_view(template_name="login.html"), name='login'),
    path('logout',LogoutView.as_view(template_name="index.html"), name='logout'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)