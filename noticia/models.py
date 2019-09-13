from django.db import models

class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=150)
    email = models.CharField('email', max_length=150)
    telefone = models.CharField('telefone', max_length=50)
    senha = models.CharField('senha', max_length=50, null=True)

    def __str__(self):
        return self.nome

class Clientes(models.Model):
    codCliente = models.CharField('cod', max_length=150)
    nome = models.CharField('nome', max_length=150)
    cpf = models.CharField('cpf', max_length=50)
    cidadeCliente= models.CharField('cidade', max_length=50)

    def __str__(self):
        return self.nome

class Autor(Usuario):
    cpf = models.CharField('CPF', max_length=50)
    escolaridade = models.CharField('Escolaridade', max_length=150)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Administrador(Usuario):
    funcao = models.CharField('funcao', max_length=200)

class Categoria(models.Model):
    titulo = models.CharField('titulo', max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    titulo = models.CharField('titulo', max_length=250)
    subtitulo = models.CharField('subtitulo', max_length=550)
    descricao = models.TextField('', max_length=550)
    data = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Functions(models.Model):
    titulo = models.CharField('titulo', max_length=250)                

    def __str__(self):
        return self.titulo    

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, 'usuario')
    titulo = models.CharField('mensagem', max_length=250)
    mensagem = models.CharField('mensage', max_length=250)
    telefone = models.CharField('telefone', max_length=30)

    def __str__(self):
        return self.titulo
