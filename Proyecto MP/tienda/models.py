from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
class Usuarios(AbstractUser):
    is_contador = models.BooleanField('Is contador', default=False)
    is_bodeguero = models.BooleanField('Is bodeguero', default=False)
    is_cliente= models.BooleanField('Is cliente',default=False)
    is_vendedor = models.BooleanField('Is vendedor', default=False)
    Comuna = models.CharField('Address',max_length=255,blank=True,null=True)
    Calle = models.CharField('calle',max_length=255,blank=True,null=True)
    cellphone = models.CharField('Cellphone',max_length=100,blank=True,null=True)
    email=models.CharField('Email',max_length=100,unique=True,null=True)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = "email"
    
    
class sedes(models.Model):
    nombreSede=models.CharField(max_length=255)
    def __str__(self):
        return self.nombreSede
    
class informecompra(models.Model):
    id=models.UUIDField(unique=True,primary_key=True, default=uuid.uuid4, editable=False)
    Nombres= models.CharField(max_length=240)
    Rut=models.IntegerField()
    Apellidos=models.CharField(max_length=240)
    Comuna=models.CharField(max_length=100,null=True, blank=True)
    Calle=models.CharField(max_length=130,null=True, blank=True)
    Sede=models.ForeignKey(sedes, on_delete=models.CASCADE,null=True, blank=True)
    Opcional=models.CharField(max_length=50,null=True, blank=True)
    Telefono=models.IntegerField(null=True, blank=True)
    def __str__(self):
        return (self.Nombres+' '+self.Apellidos)
    
class informepagosContador(models.Model):
    cantidad=models.CharField(max_length=100,default='0')   
    nombres=models.CharField(max_length=240)
    apellidos=models.CharField(max_length=240)
    