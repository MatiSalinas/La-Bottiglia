
from django.shortcuts import render
from database.models import *
from database.forms import SalidasFormulario,EntradasFormulario,EmpleadoFormulario,ProductoFormulario
from django.views.generic import DetailView
from django.contrib.admin.views.decorators import staff_member_required
def productosTemplate(request):
    productos = bottigliaDb.objects.all()
    return render(request,'productos.html',{'productos':productos})

def productosCheckbox(request):
    if request.method == 'POST':
        tipos = dict(request.POST) #convertimos en diccionario el post(es necesario para poder acceder a listas dentro de un queryobject)
        if len(tipos)==1: #Si el forms fue enviado vacio entra este if
            productos = bottigliaDb.objects.filter(tipo__icontains='')
            return render(request,'producto_check.html',{'productos':productos})
        productos = bottigliaDb.objects.filter(tipo__in=tipos['productSelect'])
        return render(request,'producto_check.html',{'productos':productos})
        
    productos = bottigliaDb.objects.filter(tipo__icontains='')
    return render(request,'producto_check.html',{'productos':productos})

def productosBusqueda(request):
    nombre_producto = request.GET['search']
    productos = bottigliaDb.objects.filter(nombre__icontains=nombre_producto)
    return render(request,'busqueda_productos.html',{'productos':productos})



def inicio(request):
    
    return render(request,'inicio.html')

def about(request):
    
    return render(request,'about.html')

def labottiglia(request):
    
    return render(request,'labottiglia.html')

@staff_member_required #se necesita ser parte del staff para acceder a estas vistas
def crear_entradas(request):
    if request.method == "POST":
        formulario = EntradasFormulario(request.POST) #tomamos los datos del formulario

        if formulario.is_valid(): #nos aseguramos que la data esta bien

            data = formulario.cleaned_data #la limpiamos

            entrada = entradas(codigo=data['codigo'],nombre=data['nombre'],fecha=data['fecha'],stock=data['stock'])

            entrada.save() #guardamos en la base de datos

            formulario = EntradasFormulario() #reiniciamos el formulario

            return render(request,'cargar_entradas.html',{'formulario':formulario})
        
    else:
        formulario = EntradasFormulario()

        return render(request,'cargar_entradas.html',{'formulario':formulario})
    

    return render(request, 'cargar_entradas.html')

@staff_member_required #se necesita ser parte del staff para acceder a estas vistas
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

@staff_member_required #se necesita ser parte del staff para acceder a estas vistas
def cargar_producto(request):
    if request.method == "POST":
        formulario = ProductoFormulario(request.POST,request.FILES)

        if formulario.is_valid():
            
            data = formulario.cleaned_data

            producto = bottigliaDb(codigo=data['codigo'],nombre=data['nombre'],entrada=data['entrada'],salida=data['salida'],stock=data['stock'],pCompra=data['pCompra'],pVenta=data['pVenta'],tipo=data['tipo'],img=data['img'])

            producto.save()

            formulario = ProductoFormulario()
            return render(request,'cargar_producto.html',{'formulario':formulario})
        else:
            return render(request,'cargar_producto.html',{'formulario':formulario,'errors':formulario.errors})
    else:
        formulario = ProductoFormulario()
        
        return render(request,'cargar_producto.html',{'formulario':formulario})
    

    return render(request, 'cargar_producto.html')

@staff_member_required #se necesita ser parte del staff para acceder a estas vistas
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

class ProductoDetail(DetailView):
    model = bottigliaDb
    template_name = 'producto_detalle.html'