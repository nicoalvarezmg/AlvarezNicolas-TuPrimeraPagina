from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from home.models import Contacto, Productos
from home.forms import CrearContacto, BuscarProducto
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

def home(request):
   return render(request, 'home/home.html')

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


def ver_producto(request, producto_id):
    producto = get_object_or_404(Productos, id=producto_id) 
    return render(request, 'home/producto.html', {'producto': producto})
 
class modificarProductoView(LoginRequiredMixin, UpdateView):
     model = Productos
     template_name = "home/modificar_producto.html"
     fields = '__all__'
     success_url = reverse_lazy('productos')
     
class eliminarProductoView(LoginRequiredMixin, DeleteView):
     model = Productos
     template_name = 'home/eliminar_producto.html' 
     success_url = reverse_lazy('productos')
   
 
   