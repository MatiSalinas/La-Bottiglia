
from django.shortcuts import render
from database.models import *

def productosTemplate(request):
    productos = bottigliaDb.objects.all()
    productos_lista = []
    for producto in productos:
        productos_lista.append(producto)
    
    return render(request,'productos.html',{'productos':productos_lista})

def contacto(request):
    
    return render(request,'contacto.html')

def inicio(request):
    
    return render(request,'inicio.html')

def labottiglia(request):
    
    return render(request,'labottiglia.html')