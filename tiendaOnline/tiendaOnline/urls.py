"""tiendaOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tiendaOnline.views import *
from django.conf.urls.static import static
import tiendaOnline.settings as settings
from database.views import *
from mensajes.views import *
from django.contrib.admin.views.decorators import staff_member_required
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name='tienda-inicio'),
    path('labottiglia/',labottiglia, name='tienda-labottiglia'),
    path('contacto/',contacto, name='tienda-contacto'),
    path('productos/',productosTemplate, name='tienda-productos'),
    path('productos/resultado',productosBusqueda,name='tienda-busqueda'),
    path('productos/check',productosCheckbox,name='tienda-check'),
    path('panel/cargar-producto',cargar_producto,name="panel-producto-nuevo"),
    
    path('productos/detail/<pk>',ProductoDetail.as_view(),name='tienda-producto-detalle'),
    path('panel/productos/',staff_member_required(ProductosList.as_view()),name='panel-productos'),
    path('panel/productos/editar/<pk>',staff_member_required(ProductosUpdate.as_view()),name='panel-productos-editar'),
    path('panel/productos/borrar/<pk>',staff_member_required(ProductosDelete.as_view()),name='panel-productos-delete'),

    #urls entradas
    path('panel/crear-entrada',crear_entradas,name="panel-entradas-nuevo"),
    path('panel/entradas/',staff_member_required(EntradasList.as_view()),name='panel-entradas'),
    path('panel/entradas/editar/<pk>',staff_member_required(EntradasUpdate.as_view()),name='panel-entradas-editar'),
    path('panel/entradas/borrar/<pk>',staff_member_required(EntradasDelete.as_view()),name='panel-entradas-delete'),

    #urls salidas

    path('panel/crear-salida',crear_salidas,name="panel-salidas-nuevo"),
    path('panel/salidas/',staff_member_required(SalidasList.as_view()),name='panel-salidas'),
    path('panel/salidas/editar/<pk>',staff_member_required(SalidasUpdate.as_view()),name='panel-salidas-editar'),
    path('panel/salidas/borrar/<pk>',staff_member_required(SalidasDelete.as_view()),name='panel-salidas-delete'),
    
    #urls empleados

    path('panel/crear-empleado',crear_empleado,name="panel-empleados-nuevo"),
    path('panel/empleados/',staff_member_required(EmpleadosList.as_view()),name='panel-empleados'),
    path('panel/empleados/editar/<pk>',staff_member_required(EmpleadosUpdate.as_view()),name='panel-empleados-editar'),
    path('panel/empleados/borrar/<pk>',staff_member_required(EmpleadosDelete.as_view()),name='panel-empleados-delete'),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)