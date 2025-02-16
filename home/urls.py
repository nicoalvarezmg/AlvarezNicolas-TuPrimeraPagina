from home.views import home, comentario, gracias
from django.urls import path


urlpatterns = [
    path('pipes-home/', home, name='pipes_home'),
    path('contacto/', comentario, name='comentario'),
    path('contacto-recibido', gracias, name='gracias')
]

