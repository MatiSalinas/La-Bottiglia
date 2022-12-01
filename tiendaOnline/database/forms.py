from django import forms
import datetime
from database.models import bottigliaDb
from django.core.exceptions import ValidationError

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

class NuevoProductoFormulario(forms.Form):
    codigo = forms.CharField()
    nombre = forms.CharField()
    entrada = forms.IntegerField()
    salida = forms.IntegerField()
    stock = forms.IntegerField()
    pCompra = forms.FloatField()
    pVenta = forms.FloatField()
    #lista con las opciones para el formulario
    TIPO_CHOICES = [
        ('VINOMALBEC' , 'Vino Malbec'),
        ('VINOBLANCO' , 'Vino Blanco'),
        ('VINOBLEND' , 'Vino Blend'),
        ('VINOCABERNET' , 'Vino Cavernet'),
        ('CHAMPANGNE' , 'Champagne'),
        ('RON' , 'Ron'),
        ('WHISKY' , 'Whisky'),
        ('APERITIVO' , 'Aperitivo'),
        ('GIN' , 'Gin'),
        ('CERVEZA' , 'Cerveza'),
        ('CRISTALERIA' , 'Cristaleria'),
        ('TEQUILA','Tequila'),
        ('VODKA' , 'Vodka'),
        ('GASEOSA' , 'Gaseosa'),
        ('JUGOS' , 'Jugos'),
        ('SNACKS' , 'Snacks'),
        ('OTRO' , 'Otro'),
    ]
    tipo = forms.ChoiceField(choices=TIPO_CHOICES)
    img = forms.ImageField()

    #nos aseguramos de que no se pueda cargar un producto con el mismo codigo
    def clean_producto(self):
        codigo = self.cleaned_data['codigo']
        print(codigo)
        if bottigliaDb.objects.filter(codigo=codigo).exists():
            raise ValidationError("Email already exists")
        return codigo



