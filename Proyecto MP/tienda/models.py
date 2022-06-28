from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Usuarios(AbstractUser):
    is_contador = models.BooleanField('Is contador', default=False)
    is_bodeguero = models.BooleanField('Is bodeguero', default=False)
    is_cliente= models.BooleanField('Is cliente',default=False)
    is_vendedor = models.BooleanField('Is vendedor', default=False)
    Comuna = models.CharField('Address',max_length=255,blank=True,null=True)
    Calle = models.CharField('calle',max_length=255,blank=True,null=True)
    cellphone = models.CharField('Cellphone',max_length=100,blank=True,null=True)
