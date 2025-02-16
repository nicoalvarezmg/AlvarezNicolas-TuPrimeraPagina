from django import forms

class CrearContacto(forms.Form):
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField()
    comentario = forms.CharField(widget=forms.Textarea, required=False)
    
    
class BuscarProducto(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
    