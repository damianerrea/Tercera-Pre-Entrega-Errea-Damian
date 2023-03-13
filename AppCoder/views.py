from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader 
from AppCoder.models import Curso

# Create your views here.
def curso(self):

    curso= Curso(nombre= "Desarrollo Web", camada= "19882")
    curso.save()
    documentoDeTexto = f"Curso: {curso.nombre} Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)
    