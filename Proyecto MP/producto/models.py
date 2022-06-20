from django.db import models
from django.utils import timezone
# Create your models here.

categoria=[
    [0, "ninguno"],
    [1, "Cuerdas"],
    [2, "Percusión"],
    [3, "Amplificadores"],
    [4, "Accesorios"]
]
class Producto(models.Model) :
    serie_producto = models.CharField(max_length=30)
    nombre = models.CharField(max_length=70)
    codigo = models.CharField(max_length=15)
    marca = models.CharField(max_length=30)
    precio = models.IntegerField(null=False, blank=True)
    imagen = models.ImageField(upload_to='img', null=True)
    categoria = models.IntegerField(choices=categoria,null=True)
    def __str__(self) :
        return f'{self.nombre} -> {self.precio}'

class Direccion(models.Model):
    idDireccion = models.CharField(max_length=30)
    calle = models.CharField(max_length=30)
    numero = models.IntegerField()
    comuna = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    depto = models.CharField(max_length=30)

    def str(self) :
        return self.calle

class Cliente(models.Model):
    serieCliente = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=10)
    correo = models.CharField(max_length=30)
    id_usuario = models.CharField(max_length=10)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def str(self):
        return self.nombre