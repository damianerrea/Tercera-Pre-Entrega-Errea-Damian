from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Curso(models.Model):

    nombre= models.CharField(max_length=40)
    camada= models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Camada: {self.camada}" 

class Estudiante(models.Model):
    nombre= models.CharField(max_length = 30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}" 

class Profesor(models.Model):
    nombre= models.CharField(max_length = 30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length = 30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profesión: {self.profesion}"  

class Entregable(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega= models.DateField()
    entregado= models.BooleanField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de entrega: {self.fechaDeEntrega}"

class Notas(models.Model):
    nombre_alumno= models.CharField(max_length=30)
    apellido_alumno= models.CharField(max_length=30)
    fecha_entrega= models.DateField()
    nota= models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return f"{self.nombre_alumno} {self.apellido_alumno} - Nota: {self.nota}"
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    