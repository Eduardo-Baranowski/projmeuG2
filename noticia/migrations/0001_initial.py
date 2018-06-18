# Generated by Django 2.0.6 on 2018-06-13 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='titulo')),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250, verbose_name='mensagem')),
                ('mensagem', models.CharField(max_length=250, verbose_name='mensage')),
                ('telefone', models.CharField(max_length=30, verbose_name='telefone')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250, verbose_name='titulo')),
                ('subtitulo', models.CharField(max_length=550, verbose_name='subtitulo')),
                ('descricao', models.TextField(max_length=550, verbose_name='')),
                ('data', models.DateField()),
                ('categoria', models.ForeignKey(on_delete='categoria', to='noticia.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('email', models.CharField(max_length=150, verbose_name='email')),
                ('telefone', models.CharField(max_length=50, verbose_name='telefone')),
                ('senha', models.CharField(max_length=50, null=True, verbose_name='senha')),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='noticia.Usuario')),
                ('funcao', models.CharField(max_length=200, verbose_name='funcao')),
            ],
            bases=('noticia.usuario',),
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='noticia.Usuario')),
                ('cpf', models.CharField(max_length=50, verbose_name='CPF')),
                ('escolaridade', models.CharField(max_length=150, verbose_name='Escolaridade')),
                ('descricao', models.TextField()),
            ],
            bases=('noticia.usuario',),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(on_delete='usuario', to='noticia.Usuario'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='autor',
            field=models.ForeignKey(on_delete='autor', to='noticia.Autor'),
        ),
    ]
