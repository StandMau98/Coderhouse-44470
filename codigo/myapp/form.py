from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    


class TorneoForm(forms.Form):
    nombre = forms.CharField()
    categoria = forms.IntegerField()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = 'Corroe electronico')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']

class UserEditForm(UserCreationForm):
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    email = forms.EmailField(label = 'Corroe electronico')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirme su Password', widget=forms.PasswordInput, required=False)
    class Meta:
        model = User
        fields = ['email','last_name', 'first_name']
        
        # ? la siguiente elimina cualquier mensaje de ayuda en los campos help_texs={k:'' for k in fields}
        help_texts = {'email': 'Indica un correo electronico que uses habitualmente', 'first_name': '', 'last_name': ''}


class AvatarForm(forms.Form):
    imagen = forms.ImageField()


