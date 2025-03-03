from django.db import models
from django.contrib.auth.models import User

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to="static/img", blank=False, null=False)
    precio = models.FloatField(blank=False, null=False)
    stock = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Producto: {self.nombre}\nPrecio: {self.precio}\n Foto: {self.foto}"
    
    
    
class Contacto(models.Model):
    email = models.EmailField()
    nombre = models.CharField(max_length=30)
    comentario = models.TextField(max_length=500, blank=True, null=True)
