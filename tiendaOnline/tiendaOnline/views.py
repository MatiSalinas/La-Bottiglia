
from django.shortcuts import render
from database.models import *
from database.forms import SalidasFormulario,EntradasFormulario,EmpleadoFormulario,NuevoProductoFormulario
import json


def productosTemplate(request):
    productos = bottigliaDb.objects.all()
    productos_lista = []
    for producto in productos:
        productos_lista.append(producto)
    
    return render(request,'productos.html',{'productos':productos_lista})

def productosCheckbox(request):
    if request.method == 'POST':
        tipos = dict(request.POST)
        if len(tipos)==1:
            productos = bottigliaDb.objects.filter(tipo__icontains='')
            return render(request,'producto_check.html',{'productos':productos})
        productos = bottigliaDb.objects.filter(tipo__in=tipos['productSelect'])
        return render(request,'producto_check.html',{'productos':productos})
        
    productos = bottigliaDb.objects.filter(tipo__icontains='snack')
    return render(request,'producto_check.html',{'productos':productos})

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

def crear_entradas(request):
    if request.method == "POST":
        formulario = EntradasFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            entrada = entradas(codigo=data['codigo'],nombre=data['nombre'],fecha=data['fecha'],stock=data['stock'])

            entrada.save()

            formulario = EntradasFormulario()

            return render(request,'cargar_entradas.html',{'formulario':formulario})

    else:
        formulario = EntradasFormulario()

        return render(request,'cargar_entradas.html',{'formulario':formulario})
    

    return render(request, 'cargar_entradas.html')

def crear_salidas(request):
    if request.method == "POST":
        formulario = SalidasFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            salida = salidas(codigo=data['codigo'],nombre=data['nombre'],fecha=data['fecha'],stock=data['stock'])

            salida.save()

            formulario = SalidasFormulario()

            return render(request,'cargar_salidas.html',{'formulario':formulario})

    else:
        formulario = SalidasFormulario()
        
        return render(request,'cargar_salidas.html',{'formulario':formulario})
    

    return render(request, 'cargar_salidas.html')

def cargar_producto(request):
    if request.method == "POST":
        formulario = NuevoProductoFormulario(request.POST,request.FILES)

        if formulario.is_valid():
            
            data = formulario.cleaned_data

            producto = bottigliaDb(codigo=data['codigo'],nombre=data['nombre'],entrada=data['entrada'],salida=data['salida'],stock=data['stock'],pCompra=data['pCompra'],pVenta=data['pVenta'],tipo=data['tipo'],img=data['img'])

            producto.save()

            formulario = NuevoProductoFormulario()
            return render(request,'cargar_producto.html',{'formulario':formulario})
            
    else:
        formulario = NuevoProductoFormulario()
        
        return render(request,'cargar_producto.html',{'formulario':formulario})
    

    return render(request, 'cargar_producto.html')

def crear_empleado(request):
    if request.method == "POST":
        formulario = EmpleadoFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            producto = empleados(nombre=data['nombre'],apellido=data['apellido'],cargo=data['cargo'],salario=data['salario'])

            producto.save()

            formulario = EmpleadoFormulario()

            return render(request,'crear_empleados.html',{'formulario':formulario})

    else:
        formulario = EmpleadoFormulario()
        
        return render(request,'crear_empleados.html',{'formulario':formulario})
    

    return render(request, 'crear_empleados.html')
