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
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/',productosTemplate, name='tienda-productos'),
    path('productos/resultado',productosBusqueda,name='tienda-busqueda'),
    path('productos/check',productosCheckbox,name='tienda-check'),
    path('contacto/',contacto, name='tienda-contacto'),
    path('',inicio, name='tienda-inicio'),
    path('labottiglia/',labottiglia, name='tienda-labottiglia'),
    path('panel/crear-entrada',crear_entradas,name="tienda-entradas"),
    path('panel/crear-salida',crear_salidas,name="tienda-salidas"),
    path('panel/crear-empleado',crear_empleado,name="tienda-empleados"),
    path('panel/cargar-producto',cargar_producto,name="tienda-producto-nuevo")

]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)