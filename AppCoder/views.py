from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader 
from AppCoder.models import Cliente, Post, Mensajes
from AppCoder.forms import ClienteFormulario , UserRegisterForm, MensajeForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def index(request):
    return render(request,"AppCoder/index.html")


def base(request):
    return render(request, "AppCoder/base.html")

@login_required
@user_passes_test(lambda u: u.is_staff)
def clientes(request):   
    if request.method == 'POST':
        miFormulario = ClienteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            clientes = Cliente(nombre= informacion['nombre'], apellido = informacion['apellido'], email= informacion['email'])
            clientes.save()
            mensaje = f"Cliente cargado exitosamente"
            return render(request, "AppCoder/index.html", {"mensaje": mensaje})     
    else:
        miFormulario = ClienteFormulario()
    
        return render(request, "AppCoder/clientes.html",{"miFormulario": miFormulario} )

def leerClientes(request):
    
    clientes = Cliente.objects.all()
    
    contexto = {"clientes": clientes}

    return render(request, "AppCoder/leerClientes.html", contexto)

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

class PostUpdate(UpdateView):
    model= Post
    success_url= "/usuario/"
    fields = ['title', 'resumen', 'content', 'image']

class PostDelete(DeleteView):
    model= Post
    success_url= "/usuario/"

class PostDetalle(DetailView):

    model= Post
    template_name= "AppCoder/post_detalle.html"

def post_list(request):
    post_list = Post.objects.all().order_by('created_at')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'AppCoder/post_list.html', {'posts': posts})

def mi_vista(request):
    next_url = request.GET.get('next', '/')
    return redirect(next_url)

def mensaje_list(request):
    mensaje_list = Mensajes.objects.all().order_by('created_at')
    paginator = Paginator(mensaje_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'AppCoder/mensaje_list.html', {'mensajes': page_obj})

@login_required
def mensajes(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensajes = form.save(commit=False)
            mensajes.author = request.user
            mensajes.save()
            return redirect('mensajes_form')
    else:
        form = MensajeForm()
    return render(request, 'AppCoder/mensajes_form.html', {'form': form})

class MensajesDelete(DeleteView):
    model= Mensajes
    success_url= "/mensaje_list/"

class MensajesUpdate(UpdateView):
    model= Mensajes
    success_url= "/mensaje_list/"
    fields = ['content']