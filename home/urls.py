from home.views import home, comentario, gracias, nuestros_productos, sobre_nosotros
from django.urls import path


urlpatterns = [
    path('pipes-home/', home, name='pipes_home'),
    path('contacto/', comentario, name='comentario'),
    path('contacto-recibido', gracias, name='gracias'),
    path('nuestros-productos', nuestros_productos, name= 'productos'),
    path('sobre-nosotros', sobre_nosotros, name='sobre_nosotros')
]

