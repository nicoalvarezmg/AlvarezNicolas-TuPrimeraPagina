from django import forms
from home.models import Productos

class CrearContacto(forms.Form):
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField()
    comentario = forms.CharField(widget=forms.Textarea, required=False)
    
    
class CrearProducto(forms.Form):
    nombre = forms.CharField(max_length=30)
    foto = forms.ImageField( required=False)
    precio = forms.FloatField()
    stock = forms.IntegerField()
    descripcion = forms.CharField(widget=forms.Textarea ,required=False)
    
    class Meta:
        model = Productos
        fields =  ['nombre', 'precio', 'stock', 'descripcion', 'foto']
    
    
class BuscarProducto(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
    