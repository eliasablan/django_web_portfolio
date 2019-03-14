# Generated by Django 2.1 on 2019-01-17 06:01

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('slug', models.SlugField(unique=True)),
                ('publicado', models.BooleanField(default=True, verbose_name='Publicado')),
                ('foto_destacada', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='albums')),
                ('descripcion', models.TextField(blank=True, max_length=500)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modificacion', models.DateTimeField(auto_now=True, verbose_name='Última Modificación')),
            ],
            options={
                'verbose_name': 'Álbum',
                'verbose_name_plural': 'Álbumes',
            },
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('slug', models.SlugField(unique=True)),
                ('publicada', models.BooleanField(default=True, verbose_name='Publicada')),
                ('imagen', imagekit.models.fields.ProcessedImageField(upload_to='fotos')),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modificacion', models.DateTimeField(auto_now=True, verbose_name='Última Modificación')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fotos', to='portafolio.Album')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
            },
        ),
    ]
