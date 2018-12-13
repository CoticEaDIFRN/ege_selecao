# Generated by Django 2.1.1 on 2018-12-06 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastroEdital', '0003_auto_20181206_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastroEdital.Edital')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifrn_id', models.CharField(help_text='Matrícula suap ou CPF', max_length=100, verbose_name='Ifrn ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
        ),
        migrations.AddField(
            model_name='coordenador',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastroEdital.Usuario'),
        ),
    ]
