from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre= models.CharField(max_length = 30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}" 
class Post(models.Model):
    title = models.CharField(max_length=200)
    resumen=models.TextField(max_length=3000, default='')
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class Mensajes(models.Model):
    content = models.TextField(max_length=3000, default='')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.content