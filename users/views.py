from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login as django_login
from home.views import home
from users.forms import CreacionUsuario, EdicionUsuario
from django.contrib.auth.decorators import login_required
from users.models import InfoExtra



def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            
            django_login(request, usuario)
            
            InfoExtra.objects.get_or_create(user=usuario)
            
            return redirect('pipes_home')
    else:
        formulario = AuthenticationForm()
        
    return render(request, 'users/login.html', {'formulario': formulario})
    
def registro(request):
    if request.method == 'POST':
        formulario = CreacionUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()            
            return redirect('login')
    else:
        formulario = CreacionUsuario()
        
    return render(request, 'users/registro.html', {'formulario': formulario})


@login_required
def ver_perfil(request):
    usuario = request.user
    return render(request, 'users/perfil.html', {
        'usuario': usuario,
        'nombre_completo': f"{usuario.first_name} {usuario.last_name}",
        'fecha_nacimiento': usuario.profile.fecha_nacimiento if hasattr(usuario, 'profile') else None,
        'avatar': usuario.profile.avatar if hasattr(usuario, 'profile') else None, 
    })

    
@login_required
def editar_perfil(request):
    
    
    info_extra = request.user.infoextra
    
    if request.method == 'POST':
        formulario = EdicionUsuario(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            if formulario.cleaned_data.get('avatar', 'fecha_nacimiento'):
                info_extra.avatar = formulario.cleaned_data.get('avatar')
                info_extra.fecha_nacimiento = formulario.cleaned_data.get('fecha_nacimiento')
                
            info_extra.save()
            formulario.save()       
                 
            return redirect('pipes_home')
    else:
        formulario = EdicionUsuario(instance=request.user, initial={'avatar': info_extra.avatar, 'fecha_nacimiento': info_extra.fecha_nacimiento})
        
    return render(request, 'users/editar_perfil.html', {'formulario': formulario})
