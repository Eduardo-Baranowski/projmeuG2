from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# Create your views here.

def home(request):
    noticia = Noticia.objects.all()
    return render(request, 'home.html', {'noticias':noticia})

@login_required
def autores(request):
    autores = Autor.objects.all()
    return render(request, 'autores.html', {'autores':autores})

def autoresAdd(request):
    return render(request, 'addAutor.html')

def salvar_autor(request):
    nome = request.POST.get('nome_autor')
    email = request.POST.get('email_autor')
    telefone = request.POST.get('telefone_autor')
    senha = request.POST.get('senha_autor')
    cpf = request.POST.get('cpf_autor')
    escolaridade = request.POST.get('escolaridade_autor')
    descricao = request.POST.get('descricao_autor')
    if cpf:
        autor = Autor()
        autor.cpf=cpf
        autor.telefone=telefone
        autor.senha=senha
        autor.nome=nome
        autor.email=email
        autor.escolaridade=escolaridade
        autor.descricao=descricao
        autor.save()
        return redirect('/autores')

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario.html', {'usuarios':usuarios})

def usuariosAdd(request, tipo):
    pagina = 'addVisitante.html'
    if(tipo ==1):
        pagina = 'addAdminstrador.html'
    if(tipo ==2):
        pagina = 'addAutor.html'
    if(tipo == 3):
        pagina = 'addVisitante.html'
    return render(request, pagina)

def salvar_usuario(request,tipo):
    nome = request.POST.get('nome_usuario')
    email = request.POST.get('email_usuario')
    telefone = request.POST.get('telefone_usuario')
    cpf = request.POST.get('cpf_usuario')
    senha = request.POST.get('senha_usuario')
    funcao = request.POST.get('funcao_usuario')
    escolaridade = request.POST.get('escolaridade_usuario')
    descricao = request.POST.get('descricao_usuario')


    if nome:
        if(tipo ==1):
            administrador = Administrador()
            administrador.nome = nome
            administrador.email = email
            administrador.telefone = telefone
            administrador.funcao = funcao
            administrador.save()
        if(tipo == 2):
            autor = Autor()
            autor.nome = nome
            autor.email = email
            autor.telefone = telefone
            autor.cpf = cpf
            autor.escolaridade = escolaridade
            autor.descricao = descricao
            autor.save()
        else:
            visitante = Usuario()
            visitante.nome = nome
            visitante.email = email
            visitante.telefone = telefone
            visitante.save()
        return redirect('/usuarios')

def excluir_usuario(request, id):
    Usuario.objects.filter(id=id).delete()
    return redirect("/usuarios")

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria.html', {'categorias':categorias})

def categoriasAdd(request):
    return render(request, 'addCategoria.html')

def salvar_categoria(request):
    titulo = request.POST.get('titulo_categoria')
    descricao = request.POST.get('descricao_categoria')
    if titulo:
        categoria = Categoria()
        categoria.titulo = titulo
        categoria.descricao=descricao
        categoria.save()
        return redirect('/categorias')

def excluir_categoria(request, id):
    Categoria.objects.filter(id=id).delete()
    return redirect('/categorias')

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    return render(request, "editarCategoria.html", {'categoria':categoria})

def editar_categoria_salvar(request,id):
    titulo = request.POST.get("titulo_categoria")
    descricao = request.POST.get("descricao_categoria")
    if titulo:
        categoria = Categoria(id)
        categoria.titulo=titulo
        categoria.descricao=descricao
        categoria.save()
        return redirect('/categorias')

def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias.html', {'noticias':noticias})

def noticiasAdd(request):
    lista_categorias = Categoria.objects.all()
    lista_autores = Autor.objects.all()
    return render(request, 'addNoticia.html', context={'categorias':lista_categorias, 'autores':lista_autores})

def noticiaId(request, id):
    noticia = Noticia.objects.get(id=id)
    return render(request, 'noticia.html', {'noticia':noticia})

def salvar_noticia(request):
    titulo = request.POST.get('titulo_noticia')
    subtitulo = request.POST.get('subtitulo_noticia')
    descricao = request.POST.get("descricao_noticia")
    data = request.POST.get("data_noticia")
    if request.method == "POST":
        varCategoria = request.POST["categoria"]
        varAutor = request.POST["autores"]
    categoria = Categoria.objects.get(pk=varCategoria)
    autor = Autor.objects.get(pk=varAutor)
    if titulo:
        noticia = Noticia()
        noticia.descricao = descricao
        noticia.titulo=titulo
        noticia.data=data
        noticia.subtitulo=subtitulo
        noticia.categoria=categoria
        noticia.autor=autor
        noticia.save()
        return redirect("/noticias")

def excluir_noticia(request, id):
    Noticia.objects.filter(id=id).delete()
    return redirect("/noticias")

def editar_noticia(request, id):
    noticia = Noticia.objects.get(id=id)
    lista_categorias = Categoria.objects.all()
    lista_autores = Autor.objects.all()
    return render(request, 'editarNoticia.html',{'noticia':noticia, 'categorias':lista_categorias, 'autores':lista_autores})

def editar_noticia_salvar(request, id):
    titulo=request.POST.get("titulo_noticia")
    subtitulo=request.POST.get("subtitulo_noticia")
    descricao=request.POST.get("descricao_noticia")
    data = request.POST.get("data_noticia")
    if request.method == "POST":
        varCategoria=request.POST['categoria']
        varAutor = request.POST['autores']
    categoria = Categoria.objects.get(pk=varCategoria)
    autor = Autor.objects.get(pk=varAutor)

    if titulo:
        noticia = Noticia(id)
        noticia.descricao=descricao
        noticia.titulo=titulo
        noticia.data=data
        noticia.subtitulo=subtitulo
        noticia.categoria=categoria
        noticia.autor=autor
        noticia.save()
        return redirect("/noticias")


def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('usuario'), password=request.POST.get('senha'))
        if user is not None:
            login(request, user)
            return redirect('/area_interna')

    return render(request, 'login.html')


@login_required
def area_interna(request):
    return render(request, 'area_interna.html', context=None)
