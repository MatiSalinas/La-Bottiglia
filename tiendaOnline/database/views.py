from django.shortcuts import render
from database.models import *



from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,UpdateView,DeleteView

# Create your views here.


#-------------ClassModelViews para producto --------------#
class ProductosList(LoginRequiredMixin,ListView):
    model = bottigliaDb
    template_name = 'panel_productos.html'


class ProductosUpdate(UpdateView):
    model = bottigliaDb
    success_url = '/panel/productos/'
    fields = ['codigo','nombre','entrada','salida','stock','pCompra','pVenta','tipo','img']
    template_name ='panel_producto_editar.html'

class ProductosDelete(DeleteView):
    model = bottigliaDb
    success_url = '/panel/productos/'
    template_name ='bottigliadb_confirm_delete.html'

#-------------ClassModelViews para entradas --------------#
class EntradasList(LoginRequiredMixin,ListView):
    model = entradas
    template_name = 'panel_entradas.html'


class EntradasUpdate(UpdateView):
    model = entradas
    success_url = '/panel/entradas/'
    fields = ['codigo','nombre','fecha','stock']
    template_name ='panel_entradas_editar.html'

class EntradasDelete(DeleteView):
    model = entradas
    success_url = '/panel/entradas/'
    template_name ='entradas_confirm_delete.html'

#-------------ClassModelViews para salidas --------------#
class SalidasList(LoginRequiredMixin,ListView):
    model = salidas
    template_name = 'panel_salidas.html'


class SalidasUpdate(UpdateView):
    model = salidas
    success_url = '/panel/salidas'
    fields = ['codigo','nombre','fecha','stock']
    template_name ='panel_salidas_editar.html'

class SalidasDelete(DeleteView):
    model = salidas
    success_url = '/panel/salidas/'
    template_name ='salidas_confirm_delete.html'

#-------------ClassModelViews para empleados --------------#
class EmpleadosList(LoginRequiredMixin,ListView):
    model = empleados
    template_name = 'panel_empleados.html'


class EmpleadosUpdate(UpdateView):
    model = empleados
    success_url = '/panel/empleados'
    fields = ['nombre','apellido','cargo','salario','fechaInsercion']
    template_name ='panel_empleados_editar.html'

class EmpleadosDelete(DeleteView):
    model = empleados
    success_url = '/panel/empleados/'
    template_name ='empleados_confirm_delete.html'