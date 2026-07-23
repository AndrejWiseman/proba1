from django.shortcuts import render

from rest_framework import viewsets
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer

# def home(request):
#     return render(request, 'index.html')



class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """
    /api/movies/          -> lista svih objavljenih filmova
    /api/movies/{slug}/    -> detalji jednog filma
    """
    queryset = Movie.objects.filter(is_published=True).prefetch_related("genres")
    serializer_class = MovieSerializer
    lookup_field = "slug"


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


