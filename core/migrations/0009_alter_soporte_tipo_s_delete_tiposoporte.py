# Generated by Django 4.0.5 on 2023-06-23 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_tiposoporte_id_tipo_s'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soporte',
            name='tipo_s',
            field=models.IntegerField(choices=[[0, 'Soporte Tecnico'], [1, 'Solicitud en linea'], [2, 'Contacto'], [3, 'Otro']]),
        ),
        migrations.DeleteModel(
            name='TipoSoporte',
        ),
    ]