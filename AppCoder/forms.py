from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class EstudianteFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email = forms.EmailField()
class EntregableFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    fechaDeEntrega=forms.DateField(label="Fecha")
    entregado = forms.BooleanField(label="¿Fue entregado?")

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']
        help_texts={k:"" for k in fields}

class NotasFormulario(forms.Form):
    nombre_alumno=forms.CharField(max_length=30)
    apellido_alumno=forms.CharField(max_length=30)
    fecha_entrega = forms.DateField()
    nota = forms.DecimalField(max_digits=2, decimal_places=1)