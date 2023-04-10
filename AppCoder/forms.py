from django import forms
from django.forms import ModelForm
from .models import Post, Mensajes
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import models

class ClienteFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email = forms.EmailField()
class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email= forms.EmailField(label="Cambiar email")
    password1=forms.CharField(label='Contraseña nueva', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir la contraseña nueva', widget=forms.PasswordInput)
    class Meta:
        model= User
        fields= ['email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'resumen',  'content', 'image']

class MensajeForm(forms.ModelForm):
    class Meta:
        model= Mensajes
        fields=['content']
