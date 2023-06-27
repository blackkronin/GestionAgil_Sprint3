"""
URL configuration for GuarderiaWEB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import home,Reserva, pagReservar,registrarse, SobreNosotros, administrador, cuidadoras , mostrar_cuidador, form_cuidador ,form_del_cuidador, form_mod_cuidador, soporte, admin_mensajes, admin_reserva, delete_hora, camara

urlpatterns = [
    path('',home,name='home'),
    path('pag-reservar/',pagReservar,name='pagReservar'),
    path('Reserva/',Reserva,name='Reserva'),
    path('registrarse/',registrarse,name='registrarse'),
    path('SobreNosotros/',SobreNosotros,name='SobreNosotros'),
    path('administrador/',administrador,name='administrador'),
    path('cuidadoras/',cuidadoras,name='cuidadoras'),
    path('mostrar_cuidador/',mostrar_cuidador,name='mostrar_cuidador'),
    path('form_cuidador/',form_cuidador,name='form_cuidador'),
    path('form_del_cuidador/<id>',form_del_cuidador,name='form_del_cuidador'),
    path('form_mod_cuidador/<id>',form_mod_cuidador,name='form_mod_cuidador'),
    path('soporte/',soporte,name='soporte'),
    path('admin_mensajes/',admin_mensajes,name='admin_mensajes'),
    path('admin_reserva/',admin_reserva,name='admin_reserva'),
    path('delete_hora/<id>',delete_hora,name='delete_hora'),
    path('camara/', camara, name='camara'),
]
