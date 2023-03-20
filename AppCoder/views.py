from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader 
from AppCoder.models import Curso, Profesor, Estudiante, Entregable
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario 

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

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre= informacion['curso'], camada = informacion['camada'])
            curso.save()
            return render(request, "AppCoder/index.html")
        
    else:
        miFormulario = CursoFormulario()
    
        return render(request, "AppCoder/cursos.html",{"miFormulario": miFormulario} )

def profesores(request):
    
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesores = Profesor(nombre= informacion['nombre'], apellido = informacion['apellido'], email= informacion['email'] , profesion= informacion['profesion'])
            profesores.save()
            return render(request, "AppCoder/index.html")
        
    else:
        miFormulario = ProfesorFormulario()
    
        return render(request, "AppCoder/profesores.html",{"miFormulario": miFormulario} )

def entregables(request):
    #return HttpResponse("Vista entregables")
    #return render(request, "AppCoder/entregables.html")
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            entregables = Entregable(nombre= informacion['nombre'], fechaDeEntrega = informacion['fechaDeEntrega'], entregado= informacion['entregado'])
            entregables.save()
            return render(request, "AppCoder/index.html")
            
    else:
        miFormulario = EntregableFormulario()
    
    return render(request, "AppCoder/entregables.html",{"miFormulario": miFormulario} )

def base(request):
    return render(request, "AppCoder/base.html")

def estudiantes(request):
    
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiantes = Estudiante(nombre= informacion['nombre'], apellido = informacion['apellido'], email= informacion['email'])
            estudiantes.save()
            return render(request, "AppCoder/index.html")
        
    else:
        miFormulario = EstudianteFormulario()
    
        return render(request, "AppCoder/estudiantes.html",{"miFormulario": miFormulario} )

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    if request.GET.get('camada'):
        camada= request.GET['camada']
        cursos= Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultadosPorBusqueda.html", {"cursos":cursos, "camada":camada})
    else:
        respuesta="No enviaste datos"
    
    return HttpResponse(respuesta)