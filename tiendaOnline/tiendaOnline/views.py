from cgitb import html
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def productosTemplate(request):
    productos_html = open('D:/Users/matil/ProyectosDjango/La_bottiglia/tiendaOnline/tiendaOnline/templates/productos.html')
    
    plantilla = Template(productos_html.read())

    productos_html.close()

    producto_context = Context()

    documento = plantilla.render(producto_context)

    return HttpResponse(documento)

def contacto(request):
    
    return render(request,'contacto.html')

def inicio(request):
    
    return render(request,'inicio.html')

def labottiglia(request):
    
    return render(request,'labottiglia.html')