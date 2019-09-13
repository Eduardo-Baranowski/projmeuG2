from django.urls import path
from .views import *

urlpatterns = [
	path('home/', home),
    path('usuarios/', selection_function),
    path('categorias/', categorias),
    path('noticias', noticias),
    path('functions/', salvar_function),
    path('funcao/', funcao),
    path('home/function/retornaCalc', retornaCalc),
    path('home/function/<int:id>', functionInsert),
    path('home/function/insert', insert_function),
    path('home/function/<int:id>', functionDelet),
    path('home/function/delet', excluir_function),
]
