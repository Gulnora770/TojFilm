import random
from .models import Movie

def random_movies(request):
    movies = list(Movie.objects.all())
    random_movies = random.sample(movies, min(15, len(movies))) if movies else []
    return {'random_movies': random_movies}