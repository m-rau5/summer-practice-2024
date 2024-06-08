from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import User, UserMovies


def registerView(request):
    if request.user.is_authenticated:
        return redirect("/users/home")
    if request.method == "GET":
        registerForm = UserCreationForm()
        return render(request, "register.html", {"form": registerForm})
    if request.method == "POST":
        if request.user.is_authenticated:
            messages.error(request, ('User already exists.'))
            print(request.user.username)
            return redirect('/')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            print("Register OK!")

            User.objects.create(username=form["username"].data)

            return redirect(request.POST.get('next', '/users/home'))
        else:
            return HttpResponse("Form is Invalid", status=400)


def loginView(request):
    if request.user.is_authenticated:
        return redirect("/users/home")
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(request.POST.get('next', '/users/home'))
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logoutView(request):
    if request.method == "GET":
        logout(request)
        return redirect("/")


@login_required(login_url="/users/login/")
def viewUserHome(request):
    if request.method == "GET":
        return redirect("/movies")


@login_required(login_url="/users/login/")
def viewUserFriends(request):
    if request.method == "GET":
        friends = []
        user = User.objects.filter(id=request.user.id).first()
        for friend in user.friends.all():
            friends.append(friend)
        return render(request, "friends.html", {'friends': friends})

    if request.method == "POST":
        friend_post = request.POST.get('friendUsername')
        friend = User.objects.filter(username=friend_post).first()
        friendsList = User.objects.filter(
            id=request.user.id).first().friends.all()
        user = User.objects.filter(id=request.user.id).first()

        if friend:
            if friend.username == request.user.username:
                return HttpResponse("Can't add yourself as friend. :(", status=400)
            for entry in friendsList:
                if entry.id == friend.id:
                    return HttpResponse("User already a friend", status=400)
            friend.friends.add(user)
            user.friends.add(friend)
            friend.save()
            return redirect('/')
        else:
            return HttpResponse("Invalid User", status=400)

    # if request.method == "DELETE":
    #     friend_post = request.POST.get('friendUsername')
    #     friend = User.objects.filter(username=friend_post).first()

    #     user = User.objects.filter(id=request.user.id).first()
    #     friendsList = User.objects.filter(
    #         id=request.user.id).first().friends.all()

    #     if friend in friendsList:
    #         user.friends.remove(friend)
    #         friend.friends.remove(user)
    #         return redirect('/')
    #     return HttpResponse("Not a friend", status=400)


@login_required(login_url="/users/login/")
def removeFriend(request, id):
    listOfFriends = []
    user = User.objects.filter(id=request.user.id).first()
    print(id)
    for friend in user.friends.all():
        print(friend)
        if friend.id == id:
            print(friend)
            continue
        else:
            # listOfFriends.append(friend)
            print("no")
    print(f"New friends :{listOfFriends}")
    return redirect("/")
