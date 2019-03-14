from django.contrib import admin
from .models import Album, Foto

class FotoInline(admin.TabularInline):
    model = Foto
    extra = 1
    prepopulated_fields = {'slug': ('titulo',)}

class AlbumAdmin(admin.ModelAdmin):
    inlines = [FotoInline, ]
    
    fieldsets = (
        ('Identificacion', {
            'fields': (
                'nombre',
                'slug',
                'publicado',
                'descripcion',
                'foto_destacada',
            )
        }),
        ('Metadata', {
            'fields': (
                ('creacion', 'modificacion'),
            )
        })
    )
    prepopulated_fields = {'slug': ('nombre',)}
    list_display_links = ('id', 'nombre')
    list_display = ('id', 'nombre', 'publicado', 'foto_destacada', 'creacion', 'modificacion')
    search_fields = ('nombre', 'slug', 'foto_destacada', 'descripcion', 'autor')
    list_filter = ('publicado', 'creacion', 'modificacion')
    readonly_fields = ('creacion', 'modificacion')

admin.site.register(Album, AlbumAdmin)

class FotoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identificacion', {
            'fields': (
                'titulo',
                'slug',
                'publicada',
                'album',
                'imagen',
            )
        }),
        ('Metadata', {
            'fields': (
                ('creacion', 'modificacion'),
            )
        })
    )
    prepopulated_fields = {'slug': ('titulo',)}
    list_display_links = ('id', 'titulo')
    list_display = ('id', 'titulo', 'publicada', 'album', 'imagen', 'creacion', 'modificacion')
    search_fields = ('titulo', 'slug', 'album', 'imagen')
    list_filter = ('publicada', 'album', 'creacion', 'modificacion')
    readonly_fields = ('creacion', 'modificacion')

admin.site.register(Foto, FotoAdmin)
