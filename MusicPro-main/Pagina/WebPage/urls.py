from django.urls import path,include,re_path
from .views import index,contact,blog,productos,about
from django.conf.urls.static import static
from django.conf import settings
#from WebPage.views import  agregar_producto, eliminar_producto, restar_producto, limpiar_carrito

urlpatterns =[
   path('',index, name='Index'),
   path('contactanos',contact, name='Contactanos'),
   path('blog',blog,name='Blog'),
   path('productos',productos,name='Product'),
   path('sobrenuestrosproductos',about,name='About'),
   #path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
   #path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
   #path('restar/<int:producto_id>/', restar_producto, name="Sub"),
   #path('limpiar/', limpiar_carrito, name="CLS"),
   
]
if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)