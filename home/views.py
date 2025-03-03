from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from home.models import Contacto, Productos
from home.forms import CrearContacto, BuscarProducto, CrearProducto
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms.widgets import ClearableFileInput


# Create your views here.

def home(request):
   return render(request, 'home/home.html')

@login_required
def comentario(request):   
   formulario = CrearContacto()
   if request.method == "POST":
      formulario = CrearContacto(request.POST)
      if formulario.is_valid():
         nombre = formulario.cleaned_data.get('nombre')
         email = formulario.cleaned_data.get('email')
         comentario = formulario.cleaned_data.get('comentario')
         
         contacto = Contacto(email = email, nombre=nombre, comentario = comentario)
         contacto.save()
         
         return redirect("gracias")    
   return render(request, 'home/comentario.html', {'formulario' : formulario})

@login_required
def gracias(request):
   return render(request, 'home/gracias.html')

def nuestros_productos(request):
   productos = Productos.objects.all()
   formulario = BuscarProducto(request.GET)
   if formulario.is_valid():
      producto_a_buscar = formulario.cleaned_data.get('nombre')
      productos = Productos.objects.filter(nombre__icontains=producto_a_buscar)
      
   return render(request, 'home/nuestros_productos.html', {'productos': productos, 'formulario': formulario})

def sobre_nosotros(request):
   return render(request, 'home/sobre_nosotros.html')

@login_required
def crear_producto(request):
   
   formulario = CrearProducto()
   
   if request.method == "POST":
      formulario = CrearProducto(request.POST, request.FILES)
      if formulario.is_valid():
         nombre = formulario.cleaned_data.get('nombre')
         precio = formulario.cleaned_data.get('precio')
         stock = formulario.cleaned_data.get('stock')
         descripcion = formulario.cleaned_data.get('descripcion')
         foto = formulario.cleaned_data.get('foto')
         producto = Productos(nombre=nombre, precio=precio, stock=stock, descripcion=descripcion, foto=foto)
         producto.save()
         
         return redirect('productos')
   return render(request, 'home/crear_producto.html', {'formulario':formulario})
         
def ver_producto(request, producto_id):
    producto = get_object_or_404(Productos, id=producto_id) 
    return render(request, 'home/producto.html', {'producto': producto})
 
     
class eliminarProductoView(LoginRequiredMixin, DeleteView):
     model = Productos
     template_name = 'home/eliminar_producto.html' 
     success_url = reverse_lazy('productos')
   
    
class ModificarProductoView(LoginRequiredMixin, UpdateView):
    model = Productos
    form_class = CrearProducto
    template_name = "home/modificar_producto.html"
    success_url = reverse_lazy('productos')

    def get_object(self, queryset=None):
        return Productos.objects.get(id=self.kwargs['pk'])
   
 
   