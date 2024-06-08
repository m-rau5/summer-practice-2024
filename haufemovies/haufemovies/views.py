from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def homepage(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return render(request, "home_default.html")
