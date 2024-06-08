from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.registerView, name="register"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('home/', views.viewUserHome, name="home"),
    path('friends/', views.viewUserFriends,  name="friends"),
    path('friends/friends/remove/<int:id>/',
         views.removeFriend, name="friends"),
]
