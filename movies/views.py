from django.shortcuts import render
from django.views import View
from .utils import get_tmdb_data

class HomePageView(View):
    def get(self, request):
        popular_movies = get_tmdb_data('movie/popular', {'language': 'en-US', 'page': 1})
        return render(request, 'movies/home.html', {'movies': popular_movies['results']})

class MovieDetailView(View):
    def get(self, request, movie_id):
        movie = get_tmdb_data(f"movie/{movie_id}", {'language': 'en-US'})
        recommendations = get_tmdb_data(f"movie/{movie_id}/recommendations", {'language': 'en-US'})
        return render(request, 'movies/detail.html', {
            'movie': movie,
            'recommendations': recommendations['results']
        })
