# Generated by Django 2.1.7 on 2019-05-08 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_civil', models.CharField(max_length=150, verbose_name='Nome Civil')),
                ('nome_social', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome Social')),
                ('nome_apresentacao', models.CharField(max_length=150, verbose_name='Nome de Apresentação')),
                ('nome_usual', models.CharField(max_length=150, verbose_name='Nome Usual')),
                ('nome_mae', models.CharField(max_length=150, verbose_name='Nome da Mãe')),
                ('nome_pai', models.CharField(max_length=150, verbose_name='Nome do Pai')),
                ('sexo', models.CharField(max_length=20, verbose_name='Sexo')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('pais_nascimento', models.CharField(max_length=100, verbose_name='País de Nascimento')),
                ('estado_nascimento', models.CharField(max_length=50, verbose_name='Estado de Nascimento')),
                ('cidade_nascimento', models.CharField(max_length=150, verbose_name='Município de Nascimento')),
                ('rg', models.PositiveIntegerField(verbose_name='RG')),
                ('data_emissao', models.DateField(verbose_name='Data de emissão')),
                ('estado_emissao', models.CharField(max_length=50, verbose_name='Estado Emissão')),
                ('orgao_rg', models.CharField(max_length=100, verbose_name='Órgão do RG')),
                ('email', models.CharField(max_length=150, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=150, verbose_name='Telefone')),
                ('cep', models.CharField(max_length=50, verbose_name='CEP')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('complemento', models.CharField(max_length=100, null=True, verbose_name='Complento')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=50, verbose_name='Estado ')),
                ('pais', models.CharField(max_length=100, verbose_name='País ')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('arquivo', models.FileField(upload_to='media/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=200, verbose_name='Número')),
                ('candidato', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inscricao.Candidato')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscricao.Documento')),
            ],
        ),
    ]
