from django.urls import path
from django.views.generic import TemplateView
from portafolio.views import HomeView, AlbumView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug>/', AlbumView.as_view(), name='album')

]
