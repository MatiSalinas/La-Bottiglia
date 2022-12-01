from django import forms
import datetime
from database.models import bottigliaDb


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




