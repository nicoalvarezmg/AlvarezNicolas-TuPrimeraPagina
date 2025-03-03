from home.views import home, comentario, gracias, nuestros_productos, sobre_nosotros, crear_producto, ver_producto, modificarProductoView, eliminarProductoView
from django.urls import path


urlpatterns = [
    path('', home, name='pipes_home'),
    path('contacto/', comentario, name='comentario'),
    path('contacto-recibido', gracias, name='gracias'),
    path('nuestros-productos', nuestros_productos, name= 'productos'),
    path('sobre-nosotros', sobre_nosotros, name='sobre_nosotros'),
    path('crear-producto/', crear_producto, name='crear_producto'),
    path('ver-producto/<int:producto_id>/', ver_producto, name="ver_productos"), 
    path('modificar-producto/<int:pk>/', modificarProductoView.as_view(), name="modificar_productos"),
    path('eliminar-producto/<int:pk>/', eliminarProductoView.as_view(), name="eliminar_productos"),
]

