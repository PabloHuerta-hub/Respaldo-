from tienda.models import Usuarios
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegistroUsuarios(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ['username','password1','password2']
        
        
class Clientes(UserCreationForm):
    email=forms.EmailField(max_length=60)
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
                    'id':'pass1'
                }
            ),
            'password2':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Confirme su contraseña',
                    'id':'pass2'
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