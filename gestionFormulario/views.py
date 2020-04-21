from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from gestionFormulario.models import Personas
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import PersonasForm
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from django.db.models import Q


# Create your views here.

# Para validar usuario y clave


def my_view(request):

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request,
                        username=username,
                        password=password)

    if user is not None:

        login(request, user)

        return render(request, 'index.html')

    else:

        return render(request, 'error.html')


# Permite salir de los usuarios.
def logout_view(request):

    logout(request)

    return render(request, 'login.html')


# Permite mandar los datos de los formularios a la tabla de la base de datos
def date_in(request):

    form = PersonasForm(request.POST or None)

    if form.is_valid():

        instance = form.save(commit=False)

        instance.user = request.user

        instance.save()

        form.clean()

        context = {
            'form': form
        }

        return render(request, 'gracias.html', context)

    else:

        form.save(IntegrityError)

        form.clean()

        return render('error_datos.html')


# Permite mostrar los datos de los formularios mandados la base de datos
def personas_datos(request):

    queryset = Personas.objects.all()

    context = {
        'object_list': queryset,

    }

    return render(request, 'registro.html', context)

# Permite mostrar los datos de los formularios buscados en la base de datos


def Looking_For_Person(request):

    if request.GET['prs']:

        persona = request.GET['prs']

        obj = Personas.objects.filter(
            Q(Nombre__icontains=persona) | Q(Apellido__icontains=persona))

        context = {
            'buscado': obj,
            'query': persona,
        }

        return render(request, 'registro.html', context)

    else:

        return HttpResponseRedirect('/registro/')


# Permite eliminar los datos por id de los formularios buscados en la base de datos
def delete(request, id):

    context = {}

    persona = get_object_or_404(Personas, id=id)

    if request.method == 'POST':

        persona.delete()

        return HttpResponseRedirect('/registro/')

    return render(request, 'delete.html', context)


# Permite actulizar los datos por id de los formularios buscados en la base de datos
def update(request, id):

    obj = get_object_or_404(Personas, id=id)

    form = PersonasForm(request.POST or None, instance=obj)

    context = {
        'form': form
    }

    if form.is_valid():

        obj = form.save(commit=False)

        obj.user = request.user

        obj.save()

        form.clean()

        return HttpResponseRedirect('/registro/')

    else:

        context = {
            'form': form
        }

        return render(request, 'update.html', context)
