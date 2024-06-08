from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('users/', include('users.urls')),
    path('movies/', include('movies.urls'))
]
