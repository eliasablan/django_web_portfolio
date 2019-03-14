import uuid
from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit
from django.contrib.auth.models import User

class Album(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    slug = models.SlugField(unique=True)

    publicado = models.BooleanField(default=True, verbose_name="Publicado")
    foto_destacada = ProcessedImageField(upload_to='albums',
                                    processors=[ResizeToFill(450, 450)],
                                    format='JPEG',
                                    options={'quality': 90},
                                    null=True,
                                    blank=True)
    descripcion = models.TextField(max_length=500, blank=True)
    
    creacion = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Fecha de Creación")
    modificacion = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Última Modificación")

    class Meta:
        verbose_name = 'Álbum'
        verbose_name_plural = 'Álbumes'

    def __str__(self):
        return self.nombre

class Foto(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="Título")
    slug = models.SlugField(unique=True)
    publicada = models.BooleanField(default=True, verbose_name="Publicada")
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, blank=True, null=True, related_name='fotos')
    imagen = ProcessedImageField(upload_to='fotos', processors=[ResizeToFit(1280)], format='JPEG', options={'quality': 70})
    imagen_450 = ImageSpecField(source='imagen',
                                processors=[ResizeToFill(450,450)],
                                format='JPEG',
                                options={'quality':80},)

    creacion = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Fecha de Creación")
    modificacion = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Última Modificación")

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

    def __str__(self):
        return self.titulo

    def albumNombre(self):
        try:
            return self.album.nombre
        except:
            return 'undefined'
    