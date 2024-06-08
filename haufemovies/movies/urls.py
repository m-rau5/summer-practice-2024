from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('recommend/', views.movieRecommender)
]
