from mailbox import NoSuchMailboxError
from pyexpat import model
from tkinter import CASCADE
from django.utils import timezone
from django.db import models
import uuid
# Create your models here.
categoria=[
    [0, "ninguno"],
    [1, "Cuerdas"],
    [2, "Percusión"],
    [3, "Amplificadores"],
    [4, "Accesorios"]
]
class Producto(models.Model) :
    serie_producto = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=30)
    codigo = models.CharField(max_length=15)
    marca = models.CharField(max_length=30)
    precio = models.IntegerField(null=False, blank=True)
    imagen = models.ImageField(upload_to='img', null=True)
    categoria = models.IntegerField(choices=categoria,null=True)
    def __str__(self) :
        return f'{self.nombre} -> {self.precio}'

