# Generated by Django 3.0.4 on 2020-04-20 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestionFormulario', '0010_auto_20200420_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
