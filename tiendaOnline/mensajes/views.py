from django.shortcuts import render,redirect
from mensajes.models import Mensajes
import datetime

# Create your views here.
def contacto(request):
    mensajes = Mensajes.objects.all()
    if request.method == 'POST':
        if len(dict(request.POST)) > 1:
            fecha1 = datetime.datetime.now()
            msg = Mensajes(sender=request.user,msg_content=request.POST['msg_input'],fecha=fecha1)
            msg.save()
        return redirect('tienda-contacto')
    return render(request,'contacto.html',{'mensajes':mensajes})