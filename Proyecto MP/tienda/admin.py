from django.contrib import admin
from tienda.models import Usuarios
from django.contrib.auth.admin import UserAdmin
from .forms import RegistroUsuarios

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model=Usuarios
    add_form=RegistroUsuarios

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User information',{
                'fields':(
                    'is_contador',
                    'is_bodeguero',
                    'is_cliente',
                    'is_vendedor',
                    'Comuna',
                    'Calle',
                    'cellphone',
                )
            }
        )
    )
admin.site.register(Usuarios,CustomUserAdmin)