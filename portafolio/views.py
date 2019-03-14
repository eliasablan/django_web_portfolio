from django.shortcuts import render
from .models import Album, Foto
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import ListView, TemplateView

class HomeView(TemplateView):

    template_name = 'principal/home.html'

    def get_context_data(self, **kwargs):

        context = super(HomeView, self).get_context_data(**kwargs)
        context['albumes'] = Album.objects.filter(publicado=True)
        return context

class AlbumView(TemplateView):

    template_name = 'principal/album.html'

    def get_context_data(self, **kwargs):

        context = super(AlbumView, self).get_context_data(**kwargs)
        context['albumes'] = Album.objects.all()
        context['album'] = Album.objects.get(slug=self.kwargs['slug'])
        context['fotos'] = Foto.objects.filter(album=context['album'])
        return context

def handler404(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 404)