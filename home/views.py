from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Contacto, Productos
from home.forms import CrearContacto, BuscarProducto

# Create your views here.

def home(request):
   return render(request, 'home/home.html')

def comentario(request):
   print(request.POST)
   
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