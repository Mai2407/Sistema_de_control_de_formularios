"""Formularios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Formularios.views import inicio, formulario, login, back_to_login, error_datos, eliminar
from gestionFormulario import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('inlogin/', views.my_view),
    path('logout/', views.logout_view),
    path('inicio/', inicio),
    path('registro/', views.personas_datos, name="registro"),
    path('buscar/', views.Looking_For_Person),
    path('formulario/', formulario),
    path('error_datos/', error_datos),
    path('date_in/', views.date_in),
    path('back/', back_to_login),
    path('<id>/delete', views.delete, name="delete"),
    path('eliminar/', eliminar),
    path('<id>/update', views.update, name="update"),

]
