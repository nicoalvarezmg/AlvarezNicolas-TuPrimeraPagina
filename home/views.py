from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
   # return HttpResponse("<h1>Hola soy la vista</h1>")
   return render(request, 'home/home.html')