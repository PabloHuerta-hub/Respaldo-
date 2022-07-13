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
from tienda.views import product,index,contact,blog,carrito,  agregar_producto, eliminar_producto,sumar_producto, limpiar_carrito, restar_producto,registrarse,FormsPago,Checkout,limpiar_compra
from tienda.views import productobodeguero,ordenesbodeguero
from tienda.views import entregascontador,pagoscontador
from tienda.views import productovendedor,pedidosvendedor,ordenesvendedor
router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
router.register(r'productos', views.ProductoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),#Autentificación de la API
    #vistas inicio
    path('',index, name='Index'),
    path('contactanos/',contact, name='Contactanos'),
    path('blog/',blog,name='Blog'),
    path('productos/',product,name='Product'),
    path('carrito/',carrito,name='carrito'),
    path('pago/',FormsPago,name='Pago'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('sumar/<int:producto_id>/', sumar_producto,name="Sum"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('limpiarcompra/', limpiar_compra, name="limpiarcompra"),
    path('checkout/',Checkout,name="Checkout"),
    #vistas registro y autenticacion
    path('login/',LoginView.as_view(template_name="Inicio/login.html"), name='login'),
    path('logout/',LogoutView.as_view(template_name="Inicio/index.html"), name='logout'),
    path('registrarse/',registrarse,name="Registrarse"),
    #vistas bodeguero
    path('productobodega/',productobodeguero,name="productobodega"),
    path('ordenesbodeguero/',ordenesbodeguero,name="ordenesbodeguero"),
    #vistas contador
    path('entregascontador/', entregascontador, name="entregascontador"),
    path('pagoscontador/', pagoscontador, name="pagoscontador"),
    #vistas vendedor
    path('productovendedor/',productovendedor,name="productovendedor"),
    path('pedidosvendedor/',pedidosvendedor,name="pedidosvendedor"),
    path('ordenesvendedor/',ordenesvendedor,name="ordenesvendedor")
    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)