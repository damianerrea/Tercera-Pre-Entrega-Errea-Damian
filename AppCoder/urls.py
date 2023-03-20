from django.urls import path
from AppCoder.views import *

urlpatterns = [
    #path('', inicio, name="inicio"),
    path("", index, name="index"),
    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),
    path('busquedaCamada', busquedaCamada, name="busquedacamada"),
    path('buscar/', buscar),
    path('base/', base)
]
