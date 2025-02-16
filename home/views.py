from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Contacto
from home.forms import CrearContacto

# Create your views here.

def home(request):
   return render(request, 'home/home.html')

def gracias(request):
   return render(request, 'home/gracias.html')

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