from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", index, name="index"),
    path('clientes/', clientes, name="clientes"),
    path('base/', base),
    path('leerClientes', leerClientes, name="leerClientes"),
    path('login', login_request, name='Login'),
    path('register', register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('usuario/', user_posts, name='user_posts'),
    path('form_post/', create_post, name='form_post'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('edit_post/', edit_post, name='edit_post'),
    path(r'^editar_post/(?P<pk>\d+)$', PostUpdate.as_view(), name='Edit_post'),
    path(r'^post_borrar/(?P<pk>\d+)$', PostDelete.as_view(), name='Delete_post'),
    path(r'^detalle/(?P<pk>\d+)$', PostDetalle.as_view(), name='Detalle'),
    path('lista_posts/', post_list, name='post_list'),
    path('mi_vista', mi_vista, name='mi_vista'),
    path('mensaje_list/', mensaje_list, name='mensaje_list'),
    path('mensajes_form', mensajes, name='mensajes_form'),
    path(r'^mensaje_borrar/(?P<pk>\d+)$', MensajesDelete.as_view(), name='Delete_mensaje'),
    path(r'^editar_mensaje/(?P<pk>\d+)$', MensajesUpdate.as_view(), name='Edit_mensaje'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)