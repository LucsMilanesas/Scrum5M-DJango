from django.db import models

class Marca(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    stock = models.IntegerField(default=0)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos",null=True)
    def __str__(self):
        return self.nombre  