from django.urls import path
from users.views import login, registro, ver_perfil, editar_perfil, CambiarPasswordView, cambio_exitoso
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),
    path('ver-perfil/', ver_perfil, name='ver_perfil'),
    path('editar-perfil/', editar_perfil, name='editar_perfil'),
    path('cambiar-contraseña/', CambiarPasswordView.as_view(), name='cambiar_contraseña'),
    path('contraseña-actualizada-correctamente/', cambio_exitoso, name='cambio_exitoso'),
] 
