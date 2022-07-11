from tienda.models import Usuarios, informecompra,sedes
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegistroUsuarios(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ['username','password1','password2']
        
        
class Clientes(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','Comuna','Calle','cellphone' )
        labels={
            'username':'Nombre de usuario',
            'first_name':'Primer Nombre', 
            'last_name':'Apellido', 
            'email':'Corre electronico', 
            'password1':'Contraseña', 
            'password2':'Confirmacion de contraseña',
            'Comuna':'Comuna',
            'Calle':'Calle',
            'cellphone':'Telefono'}
        widgets={
            'username':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su nombre de usuario',
                    'id':'username'
                }
            ),
            'first_name':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su primer nombre',
                    'id':'nombre'
                }
            ),
            'last_name':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su apellido',
                    'id':'apellido'
                }
            ),
            'email':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su Corre electronico',
                    'id':'email'
                }
            ),
            'password1':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su contraseña',
                    'id':'contraseña'
                }
            ),
            'password2':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Confirme su contraseña',
                    'id':'contraseña2'
                }
            ),
            'Comuna':forms.TextInput(
                attrs={
                     'class': 'form-control',
                    'placeholder':'Ingrese su Comuna',
                    'id':'Comuna'
                }
            ),
            'Calle':forms.TextInput(
                attrs={
                     'class': 'form-control',
                    'placeholder':'Ingrese su Calle',
                    'id':'Calle'
                }
            ),
            'cellphone':forms.TextInput(
                attrs={
                     'class': 'form-control',
                    'placeholder':'Ingrese su telefono',
                    'id':'telefono'
                }
            )}

class Compras(forms.ModelForm):

    class Meta:
        
        model=informecompra        
        fields=['Nombres','Apellidos','Rut','Comuna','Calle','Sede','Opcional','Telefono']
        labels={
            'Nombres':'Nombres',
            'Apellidos':'Apellidos',
            'Rut':'Rut',
            'Comuna':'Comuna',
            'Calle':'Calle',
            'Sede':'Sede',
            'Opcional':'Opcional',
            'Telefono':'Telefono',
        }
        widgets={
            'Nombres':forms.TextInput(
            attrs={'class':'form-control', 
                   'placeholder':'Ingrese sus dos nombres',
                   'id':'nombres'}
            ),
            'Apellidos':forms.TextInput(
                attrs={'class':'form-control', 
                   'placeholder':'Ingrese sus dos apellidos',
                   'id':'apellidos'}
            ),
            'Rut': forms.TextInput(
                attrs={'class':'form-control', 
                   'placeholder':'Ingrese su rut',
                   'id':'rut'}
            ),
            'Comuna':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su comuna',
                    'id':'comuna'
                    }),
            'Calle':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su calle',
                    'id':'calle'
                }
            ),
            'Opcional':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese datos extras',
                    'id':'opcional'
                }
            ),
            'Telefono':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su telefono',
                    'id':'telefono'
                }
            ),
        }