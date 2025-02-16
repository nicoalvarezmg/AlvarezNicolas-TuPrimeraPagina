from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    foto = models.URLField(blank=False, null=False)
    precio = models.FloatField(blank=False, null=False)
    stock = models.IntegerField(blank=True, null=True)
    
    
class Contacto(models.Model):
    email = models.EmailField()
    nombre = models.CharField(max_length=30)
    comentario = models.TextField(max_length=500, blank=True, null=True)