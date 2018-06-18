#from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
	path('home/', home),
    path('autenticar/', do_login, name='autenticar'),
    path('area_interna/', area_interna, name='area_interna'),
    path('autores', autores),
    path('autores/add/', autoresAdd),
    path('autores/salvar/', salvar_autor),
    path('usuarios/', usuarios),
    path('usuario/salvar/<int:tipo>', salvar_usuario),
    path('usuario/add/<int:tipo>', usuariosAdd),
    path('usuarios/excluir/<int:id>', excluir_usuario),
    path('categorias/', categorias),
    path('categorias/add', categoriasAdd),
    path('categoria/salvar', salvar_categoria),
    path('categorias/excluir/<int:id>', excluir_categoria),
    path('categorias/editar/categorias/editar/categoria/editar_categoria_salvar/<int:id>', editar_categoria_salvar),
    path("categorias/editar/<int:id>", editar_categoria),
    path('noticias', noticias),
    path('noticias/add', noticiasAdd),
    path('noticia/salvar', salvar_noticia),
    path("noticias/excluir/<int:id>", excluir_noticia),
    path("noticias/editar/<int:id>", editar_noticia),
    path("noticia/editar_noticia_salvar/<int:id>", editar_noticia_salvar),
    path('home/noticia/<int:id>', noticiaId),
]
