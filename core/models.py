from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hora(models.Model):
    codigo = models.AutoField(primary_key=True,verbose_name='Codigo')
    nombrehijo = models.CharField(max_length=50, verbose_name='Nombre Hijo')
    ruthijo = models.CharField(max_length=12,verbose_name='Rut Hijo')
    fecha = models.CharField(max_length=100,verbose_name='Fecha')
    horas_reserva = models.IntegerField(verbose_name='Cantidad de Horas')

    def __str__(self):
        return str(self.codigo)


class Cuidador(models.Model):
    rut = models.CharField(max_length=10 ,primary_key=True, verbose_name='Rut de cuidador')
    nombre = models.CharField(max_length=40, verbose_name='Nombre de cuidador')
    edad = models.IntegerField(verbose_name='Edad de cuidador')
    email = models.CharField(max_length=40, verbose_name='Email de cuidador')
    numero = models.IntegerField(verbose_name='Numero de telefono')
    dire = models.CharField(max_length=100,  verbose_name='Dirección')
    experiencia = models.CharField(max_length=500, verbose_name='Experiencia')
    calificacion = models.IntegerField(default=1,verbose_name='Calificacion cuidador')
    imagen = models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen de cuidador')

    def __str__(self):
        return self.rut

tipo_soporte = [
    [0,"Soporte Tecnico"],
    [1,"Solicitud en linea"],
    [2,"Contacto"],
    [3,"Otro"]
]

class Soporte(models.Model):
    codigo_s = models.AutoField(primary_key=True,verbose_name='Codigo')
    email_s = models.EmailField(max_length=50, verbose_name='Email')
    tipo_s = models.IntegerField(choices=tipo_soporte)
    contexto_s = models.CharField(max_length=600,verbose_name='Información del problema o consulta')

    def __str__(self):
        return str(self.codigo_s)