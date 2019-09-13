from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import pymysql.cursors

hostName        = "localhost"
userName        = "root"
userPassword    = ""
databaseName    = "testeG4"
databaseCharset = "utf8mb4"
cusrorType      = pymysql.cursors.DictCursor

databaseConnection   = pymysql.connect(host=hostName, user=userName, password=userPassword, db=databaseName, charset=databaseCharset, cursorclass=cusrorType)

def home(request):
    function = Functions.objects.all()
    return render(request, 'home.html', {'functions':function})

@login_required

def salvar_function(request):
    titulo = request.POST.get('titulo')
    
    if cpf:
        functions = Functions()
        functions.titulo=titulo
        functions.save()
        return redirect('/functions')

def functions(request):
    functions = Functions.objects.all()
    return render(request, 'home.html', {'functions':functions})

def categorias(request):    
    return render(request, 'addCategoria.html',)

def funcao(request):    
    return render(request, 'funcao.html',)

def noticias(request):
    return render(request, 'noticias.html')

def functionDelet(request, id):
    function = Functions.objects.get(id=id)
    return render(request, 'paraDelet.html', {'function':function})

def excluir_function(request):
    cursor = databaseConnection.cursor()
    getId = request.POST.get('cod')
    getId = int(getId)
    cursor.execute("call paraDelet({})".format(getId))
    databaseConnection.commit()
    cursor.close()
    return redirect('/home')

def functionSelect(request, id):
    function = Functions.objects.get(id=id)
    return render(request, 'paraDelet.html', {'function':function})

def selection_function(request):
    clientes = Clientes.objects.all()
    cursor = databaseConnection.cursor()
    cursor.execute("call paraSelect()")
    cliente = cursor.fetchall()        
    databaseConnection.commit()
    cursor.close()  
    return render(request, 'usuario.html', context = {'clientes':cliente})
    
def functionInsert(request, id):
    function = Functions.objects.get(id=id)
    return render(request, 'paraInsert.html', {'function':function})

def retornaCalc(request):
    cursor = databaseConnection.cursor()
    getId = request.POST.get('cod')        
    cursor.execute(("select retornaCalc({}) as result").format(getId))
    result = cursor.fetchone() ['result']
    databaseConnection.commit()
    cursor.close()
    return render(request, 'addNoticia.html', context = {'result':result})

def insert_function(request):
    cursor = databaseConnection.cursor()    
    getCod = request.POST.get('cod')    
    getCod = int(getCod)    
    getCod2 = request.POST.get('cod')    
    getNome = request.POST.get("nome")
    getNome = str(getNome)
    getCpf = request.POST.get("cpf")
    getCidade = request.POST.get("cidade")    
    cursor.callproc('paraInsert', [getCod, str(getNome), str(getCpf), str(getCidade)])    
    databaseConnection.commit()    
    cursor.close()
    return redirect('/home')

def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('usuario'), password=request.POST.get('senha'))
        if user is not None:
            login(request, user)
            return redirect('/area_interna')

    return render(request, 'login.html')
