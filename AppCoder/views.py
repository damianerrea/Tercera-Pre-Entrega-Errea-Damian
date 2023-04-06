from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader 
from AppCoder.models import Curso, Profesor, Estudiante, Entregable, Notas
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario, UserRegisterForm, NotasFormulario 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User



# Create your views here.

def index(request):
    return render(request,"AppCoder/index.html")

def blog(request):
    return render(request,"AppCoder/blog.html")

@login_required
@user_passes_test(lambda u: u.is_staff)
def cursos(request):
    
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre= informacion['curso'], camada = informacion['camada'])
            curso.save()
            mensaje="Curso cargado correctamente"
            return render(request, "AppCoder/cursos.html", {"miFormulario": CursoFormulario(), "mensaje": mensaje})
        
    else:
        miFormulario = CursoFormulario()
        return render(request, "AppCoder/cursos.html",{"miFormulario": miFormulario} )

@login_required
@user_passes_test(lambda u: u.is_staff)
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

@login_required
@user_passes_test(lambda u: u.is_staff)
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

def leerEstudiantes(request):
    
    estudiantes = Estudiante.objects.all()
    
    contexto = {"estudiantes": estudiantes}

    return render(request, "AppCoder/leerEstudiantes.html", contexto)

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

def leerProfesores(request):
    
    profesores = Profesor.objects.all()
    
    contexto = {"profesores": profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)

class CursoList(ListView):
    
    model= Curso
    template_name = "AppCoder/cursos_list.html"

class CursoDetalle(DetailView):

    model= Curso
    template_name= "AppCoder/curso_detalle.html"

class CursoCreacion(CreateView):

    model= Curso
    success_url= "/curso/list"
    fields= ['nombre','camada']

class CursoUpdate(UpdateView):
    model= Curso
    success_url= "/curso/list"
    fields = ['nombre', 'camada']

class CursoDelete(DeleteView):
    model= Curso
    success_url= "/curso/list"

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                mensaje = f"Bienvenido {usuario}"
                return render(request, "AppCoder/index.html", {"mensaje": mensaje})
            else:
                mensaje = "Datos incorrectos"
                return render(request, "AppCoder/index.html", {"mensaje": mensaje})

        else:
            mensaje = "Formulario erróneo"
            return render(request, "AppCoder/login.html", {"form": form, "mensaje": mensaje})

    form = AuthenticationForm()
    return render(request, "AppCoder/login.html", {"form": form})

# Vista de registro
def register(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  #username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/index.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            form = UserRegisterForm()           

      return render(request,"AppCoder/registro.html" ,  {"form":form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def notas(request):
    
    if request.method == 'POST':
        miFormulario = NotasFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            notas = Notas(nombre_alumno= informacion['nombre_alumno'], apellido_alumno = informacion['apellido_alumno'], fecha_entrega= informacion['fecha_entrega'] , nota= informacion['nota'])
            notas.save()
            mensaje= "Nota cargada correctamente"
            return render(request, "AppCoder/notas.html", {"miFormulario": NotasFormulario(), "mensaje": mensaje})
        
    else:
        miFormulario = NotasFormulario()
    
        return render(request, "AppCoder/notas.html",{"miFormulario": miFormulario} )

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'AppCoder/create_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('post_detail', pk=post.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})

@login_required
def user_posts(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    return render(request, 'AppCoder/user_posts.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'AppCoder/post_detail.html', {'post': post})