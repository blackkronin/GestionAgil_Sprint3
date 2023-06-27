from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login
from .forms import CustomUserCreationForm , CuidadorForm, SoporteForm
from .models import Hora, Cuidador, Soporte
from datetime import datetime
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def SobreNosotros(request):
    return render(request, 'core/SobreNosotros.html')

@login_required
def admin_reserva(request):
    hora = Hora.objects.all()
    datos = {
        'hora': hora
    }
    return render(request, 'core/admin_reserva.html', datos)


def delete_hora(request,id):
    hora = Hora.objects.get(codigo=id)
    hora.delete()
    messages.success(request, "Hora eliminada exitosamente")
    return redirect('admin_reserva')
    

@login_required
def soporte(request):
    if request.method == 'POST':
        soporte_form = SoporteForm(request.POST, request.FILES)

        if soporte_form.is_valid():
            soporte_form.save()
            messages.success(request, "Su mensaje se envio exitosamente, se le repondera lo mas breve posible mediante correo electronico")
            return redirect ('home')

    else:
        soporte_form = SoporteForm()
    return render(request, 'core/soporte.html' ,{'soporte_form': soporte_form })


@login_required
def admin_mensajes(request):
    soporte = Soporte.objects.all()
    datos = {
        'soporte': soporte
    }
    return render(request, 'core/admin_mensajes.html', datos)


@login_required
def administrador(request):
    return render(request, 'core/administrador.html')

@login_required
def pagReservar(request):
    horas = Hora.objects.all()
    datos={
        'horas': horas
    }
    return render(request, 'core/pag-reservar.html', datos)

@login_required
def cuidadoras(request):
    cuidador = Cuidador.objects.all()
    datos = {
        'cuidador': cuidador
    }
    return render(request, 'core/cuidadoras.html', datos)

@login_required
def mostrar_cuidador(request):
    cuidador = Cuidador.objects.all()
    datos2 = {
        'cuidador': cuidador
    }
    return render(request, 'core/mostrar_cuidador.html', datos2)


@login_required
def Reserva(request):
    horas = Hora.objects.all()
    datos={
        'horas': horas
    }
   
    nombrehijo = request.POST['nombrehijo']
    ruthijo = request.POST['ruthijo']
    fecha = request.POST['fecha']
    horas_reserva = request.POST['horas_reserva']

    horas = Hora.objects.create(nombrehijo = nombrehijo, ruthijo = ruthijo, fecha = fecha, horas_reserva = horas_reserva)
    messages.success(request, "Hora tomada exitosamente, le enviamos un correo de confirmación de su hora")
    return render(request, 'core/pag-reservar.html',datos)


def registrarse(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data = request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    return render(request, 'registration/register.html',data)



@login_required
def form_cuidador(request):                             
    if request.method == 'POST':
        cuidador_form = CuidadorForm(request.POST, request.FILES)

        if cuidador_form.is_valid():
            cuidador_form.save()
            messages.success(request, "Cuidador creado exitosamente")
            return redirect ('mostrar_cuidador')

    else:
        cuidador_form = CuidadorForm()
    return render(request, 'core/form_crear_cuidador.html' ,{'cuidador_form': cuidador_form })



def form_del_cuidador(request,id):
    cuidador = Cuidador.objects.get(rut=id)
    cuidador.delete()
    messages.success(request, "Cuidador eliminado correctamente")
    return redirect('mostrar_cuidador')


def form_mod_cuidador(request, id):
    cuidador = Cuidador.objects.get(rut=id)
    datos3 = {
        'form2': CuidadorForm(instance = cuidador)
    }
    if request.method=='POST':
        formulario = CuidadorForm(data=request.POST, instance = cuidador)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cuidador Modificado con exito")
            return redirect ('mostrar_cuidador')
        
    return render(request, 'core/form_mod_cuidador.html', datos3)


@login_required
def camara(request):
    return render(request, 'core/camara.html')