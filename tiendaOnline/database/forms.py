from django import forms
import datetime

class EmpleadoFormulario(forms.Form):
    nombre= forms.CharField()
    apellido = forms.CharField()
    cargo = forms.CharField()
    salario = forms.IntegerField()




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

class CheckBoxForm(forms.Form):
    TIPO_CHOICES = [
        ('VINO MALBEC' , 'VinoMalbec'),
        ('VINO BLANCO' , 'VinoBlanco'),
        ('VINO BLEND' , 'VinoBlend'),
        ('VINO CABERNET' , 'VinoCavernet'),
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
        ('OTROs' , 'Otro'),
    ]
    tipos = forms.CheckboxSelectMultiple(choices=TIPO_CHOICES)
