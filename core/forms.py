from django import forms  
from django.forms import ModelForm
from django.forms import widgets
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from .models import Cuidador, Soporte

class CustomUserCreationForm(UserCreationForm):  
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class CuidadorForm(forms.ModelForm):

    class Meta: 
        model= Cuidador
        fields = ['rut', 'nombre', 'edad','email','numero', 'dire' , 'experiencia','calificacion', 'imagen']
        labels ={
            'rut': 'Rut Cuidador:', 
            'nombre': 'Nombre y apellido:', 
            'edad': 'Edad:', 
            'email': 'Email:', 
            'numero': 'Numero Telefonico:',
            'dire': 'Dirección:',
            'experiencia': 'Experiencia:',
            'calificacion': 'Calificacion',
            'imagen': 'Foto:',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Sin puntos y con guión', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre y apellido', 
                    'id': 'nombre'
                }
            ), 
            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese edad', 
                    'id': 'edad'
                }
            ), 
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Email', 
                    'id': 'email'
                }
            ), 
            'numero': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese numero telefonico', 
                    'id': 'numero'
                }
            ),
            'dire': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Dirección', 
                    'id': 'dire'
                }
            ), 
            'experiencia': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese experiencia', 
                    'id': 'experiencia'
                }
            ), 
            'calificacion':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingrese calificacion', 
                    'id': 'calificacion'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Descipcion del producto', 
                    'id': 'imagen'
                }
            )

        }



class SoporteForm(forms.ModelForm):

    class Meta: 
        model= Soporte
        fields = ['email_s', 'tipo_s', 'contexto_s']
        labels ={
            'email_s': 'Ingrese su email:', 
            'tipo_s': 'Seleccione el tipo:', 
            'contexto_s': 'De información:', 
        }
        widgets={
            'email_s': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'ejemplo@duocuc.cl', 
                    'id': 'email_s'
                }
            ), 
            'tipo_s': forms.Select(
                attrs={
                    'class': 'form-control', 
                    'id': 'tipo_s'
                }
            ),  
            'contexto_s': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Escriba detalladamente el problema o solicitud', 
                    'id': 'contexto_s'
                }
            ), 


        }