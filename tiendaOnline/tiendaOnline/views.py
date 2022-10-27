from cgitb import html
from django.http import HttpResponse
from django.template import Template, Context

def productosTemplate(request):
    productos_html = open('D:/Users/matil/ProyectosDjango/La_bottiglia/tiendaOnline/tiendaOnline/templates/productos.html')
    
    plantilla = Template(productos_html.read())

    productos_html.close()

    producto_context = Context()

    documento = plantilla.render(producto_context)

    return HttpResponse(documento)