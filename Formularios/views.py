from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Funciona visualizar a la pagina princiapl
@login_required
def inicio(request):

    return render(request, 'index.html')


class secret_page(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

# Funciona visualizar el formulario page.
@login_required
def formulario(request):

    return render(request, 'formulario.html')


class secret_page(LoginRequiredMixin, TemplateView):
    template_name = 'formulario.html'


# Funciona visualizar el login page.
def login(request):

    return render(request, 'login.html')

# Si introduce los datos correcto en el formulario.
@login_required
def gracias(request):

    return render(request, 'gracias.html')


class secret_page(LoginRequiredMixin, TemplateView):
    template_name = 'gracias.html'


# En caso de introducir mal el usuario o contraseña.
def back_to_login(request):

    return render(request, 'error.html')


# En caso de introducir un dato mal
@login_required
def error_datos(request):

    return render(request, 'error_datos.html')

@login_required
def eliminar(request):

    return render(request, 'delete.html')


class secret_page(LoginRequiredMixin, TemplateView):
    template_name = 'delete.html'
