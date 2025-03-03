from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class CreacionUsuario(UserCreationForm):
   email = forms.EmailField()
   password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
   password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
   
   class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']
       help_texts = {field: '' for field in fields}
       
class EdicionUsuario(UserChangeForm):
   password = None
   email = forms.EmailField()
   first_name = forms.CharField(label="Nombre")
   last_name = forms.CharField(label="Apellido")
   fecha_nacimiento = forms.DateField(required=False, label="Fecha de Nacimiento")
   avatar = forms.ImageField(required=False, label='Foto de Perfil')
   
   
   class Meta:
       model = User
       fields = ['email', 'first_name', 'last_name', 'fecha_nacimiento', 'avatar']