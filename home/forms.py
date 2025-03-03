from django import forms
from home.models import Productos
from django.forms.widgets import ClearableFileInput

class CrearContacto(forms.Form):
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField()
    comentario = forms.CharField(widget=forms.Textarea, required=False)
    
class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = "Borrar imagen"
    initial_text = ""
    input_text = ""  

  
class CrearProducto(forms.ModelForm):  
    class Meta:
        model = Productos
        fields = ['nombre', 'precio', 'stock', 'descripcion', 'foto']
    
    foto = forms.ImageField(widget=CustomClearableFileInput, required=False)
        
   
    
class BuscarProducto(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
    