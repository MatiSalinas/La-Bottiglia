from django import forms
import datetime
from database.models import bottigliaDb
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EmpleadoFormulario(forms.Form):
    nombre= forms.CharField()
    apellido = forms.CharField()
    cargo = forms.CharField()
    salario = forms.IntegerField()
    fechaInsercion = forms.DateField(initial=datetime.date.today)




class EntradasFormulario(forms.Form):
    codigo = forms.CharField()
    nombre = forms.CharField()
    fecha = forms.DateField(initial=datetime.date.today)
    stock = forms.IntegerField()

class SalidasFormulario(forms.Form):
    codigo = forms.CharField()
    nombre = forms.CharField()
    fecha = forms.DateField(initial=datetime.date.today) 
    stock = forms.IntegerField()

class ProductoFormulario(forms.ModelForm):
    class Meta:
        model = bottigliaDb
        fields = ['codigo','nombre','entrada','salida','stock','pCompra','pVenta','tipo','img']
        
        
class UserRegisterForm(UserCreationForm):
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    email = forms.EmailField(label='Correo electronico')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme el password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', 'password1', 'password2']
    
    
class UserEditForm(UserCreationForm):
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    email = forms.EmailField(label='Correo electronico')
    edad = forms.IntegerField(label='Edad')
    telefono = forms.IntegerField(label='Telefono')
    localidad = forms.CharField(label='Tu Localidad')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirme el password', widget=forms.PasswordInput, required=False)
   
    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'edad', 'telefono', 'localidad']

        
        help_texts = { 'email': 'Indica un correo electronico que uses habitualmente', 'first_name': '', 'last_name': '', 'password1': '', 'edad': '', 'localidad': '', 'telefono': ''}


class AvatarForm(forms.Form):
    imagen = forms.ImageField()

