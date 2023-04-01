from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", index, name="index"),
    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),
    path('busquedaCamada', busquedaCamada, name="busquedacamada"),
    path('buscar/', buscar),
    path('base/', base),
    path('leerProfesores', leerProfesores, name="LeerProfesores"),
    path('leerEstudiantes', leerEstudiantes, name="leerEstudiantes"),
    path('profesorFormulario/', ProfesorFormulario, name="profesorFormulario"),
    path('curso/list', CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', CursoDelete.as_view(), name='Delete'),
    path('login', login_request, name='Login'),
    path('register', register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('blog', blog, name='blog'),
    path('notas', notas, name= "notas"),
]
