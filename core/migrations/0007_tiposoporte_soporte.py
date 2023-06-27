# Generated by Django 4.0.5 on 2023-06-23 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_hora_delete_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoSoporte',
            fields=[
                ('id_tipo_s', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de tipo o categoria')),
                ('n_tipo_s', models.CharField(max_length=50, verbose_name='Nombre de tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Soporte',
            fields=[
                ('codigo_s', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo')),
                ('email_s', models.EmailField(max_length=50, verbose_name='Email')),
                ('contexto_s', models.CharField(max_length=600, verbose_name='Información del problema o consulta')),
                ('tipo_s', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tiposoporte')),
            ],
        ),
    ]
