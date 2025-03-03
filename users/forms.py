from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import ClearableFileInput

class CreacionUsuario(UserCreationForm):
   email = forms.EmailField()
   password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
   password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
   
   class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']
       help_texts = {field: '' for field in fields}

class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = "Borrar imagen"
    initial_text = ""
    input_text = "" 
       
class EdicionUsuario(UserChangeForm):
   password = None
   email = forms.EmailField()
   first_name = forms.CharField(label="Nombre")
   last_name = forms.CharField(label="Apellido")
   fecha_nacimiento = forms.DateField(
        required=False, 
        label="Fecha de Nacimiento",
        widget=forms.DateInput(attrs={'type': 'date'}) 
   )
   avatar = forms.ImageField(required=False, label='Foto de Perfil', widget=CustomClearableFileInput)
   
   
   class Meta:
       model = User
       fields = ['email', 'first_name', 'last_name', 'fecha_nacimiento', 'avatar']
       
class MiEdicionDePassword(PasswordChangeForm):
    old_password = forms.CharField(
        label="Contraseña Actual",  # Cambia el label
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
        help_text=None,  # Elimina el help text
    )
    new_password1 = forms.CharField(
        label="Nueva Contraseña",  # Cambia el label
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=None,  # Elimina el help text
    )
    new_password2 = forms.CharField(
        label="Confirmar Nueva Contraseña",  # Cambia el label
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=None,  # Elimina el help text
    )

