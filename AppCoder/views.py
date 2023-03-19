from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader 
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario 

# Create your views here.
def inicio(request):
    #return HttpResponse("Vista inicio")
    return render(request, "AppCoder/inicio.html")

def index(request):
    return render(request,"AppCoder/index.html")

def cursos(request):
    
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre= informacion['curso'], camada = informacion['camada'])
            curso.save()
            return render(request, "AppCoder/index.html")
        
    else:
        miFormulario = CursoFormulario()
    
        return render(request, "AppCoder/cursos.html",{"miFormulario": miFormulario} )

    #return render(request, "AppCoder/cursos.html")

def profesores(request):
    #return HttpResponse("Vista profesores")
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    #return HttpResponse("Vista estudiantes")
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    #return HttpResponse("Vista entregables")
    return render(request, "AppCoder/entregables.html")

def base(request):
    return render(request, "AppCoder/base.html")

def cursoFormulario(request):

    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre= informacion['curso'], camada = informacion['camada'])
            curso.save()
            return render(request, "AppCoder/index.html")
        
    else:
        miFormulario = CursoFormulario()
    
        return render(request, "AppCoder/cursoFormulario.html",{"miFormulario": miFormulario} )
