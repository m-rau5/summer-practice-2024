from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    description = models.TextField()
    director = models.CharField(max_length=30)
    image_link = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title
