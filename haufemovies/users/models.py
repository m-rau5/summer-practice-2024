from django.db import models
from movies.models import Movie


class User(models.Model):
    username = models.CharField(max_length=30)
    friends = models.ManyToManyField("User", blank=True)

    def __str__(self) -> str:
        return self.username


class UserMovies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        user = self.user.username
        movie = self.movie.title
        relationship = user + ' - ' + movie
        return relationship
