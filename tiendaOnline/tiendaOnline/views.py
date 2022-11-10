
from django.shortcuts import render
from database.models import *
# from database.forms import SalidasFormulario,EntradasFormulario,EmpleadoFormulario

def productosTemplate(request):
    productos = bottigliaDb.objects.all()
    productos_lista = []
    for producto in productos:
        productos_lista.append(producto)
    
    return render(request,'productos.html',{'productos':productos_lista})

def productosBusqueda(request):
    nombre_producto = request.GET['search']
    productos = bottigliaDb.objects.filter(nombre__icontains=nombre_producto)
    return render(request,'busqueda_productos.html',{'productos':productos})

def contacto(request):
    
    return render(request,'contacto.html')

def inicio(request):
    
    return render(request,'inicio.html')

def labottiglia(request):
    
    return render(request,'labottiglia.html')
    