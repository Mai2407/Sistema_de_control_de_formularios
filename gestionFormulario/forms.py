from django import forms

from .models import Personas


class PersonasForm(forms.ModelForm):
    class Meta:

        model = Personas
        fields = [
            'Nombre',
            'Apellido',
            'Cedula',
            'Direccion',
            'Colegio_Electoral',
            'CentroDeVotacion',
            'Sexo',
            'Telefono',
            'Email',
            'Edad',
            'Sector'
        ]
