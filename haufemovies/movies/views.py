from django.shortcuts import render, redirect
from .models import Movie
from django.contrib.auth.decorators import login_required
from users.models import UserMovies
import pandas as pd
from static.scripts.content_based import movieRecommenderScript


@login_required(login_url="/users/login/")
def movie_list(request):
    movie_set = []
    movies = UserMovies.objects.filter(user=request.user.id)
    for entry in movies:
        movie_set.append(entry.movie)
    return render(request, 'movies.html', {'movies': movie_set})


def movieRecommender(request):
    movies = Movie.objects.all().values()
    df = pd.DataFrame(list(movies))
    df = df[['id', 'title', 'genre', 'description']]
    movieRecommenderScript(df)
    return redirect('/')
