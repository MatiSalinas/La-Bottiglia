from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class empleados(models.Model):
    nombre = models.CharField(max_length =50)
    apellido = models.CharField(max_length =50)
    cargo = models.CharField(max_length =50)
    salario = models.IntegerField()
    fechaInsercion = models.DateField(null=True,blank=True)

    def __str__(self):
        return f'{self.apellido} -- {self.cargo}'

class entradas(models.Model):
    codigo = models.CharField(max_length = 50)
    nombre = models.CharField(max_length = 50)
    fecha = models.DateField()
    stock = models.IntegerField()

class salidas(models.Model):
    codigo = models.CharField(max_length = 50)
    nombre = models.CharField(max_length = 50)
    fecha = models.DateField()
    stock = models.IntegerField()
    
class bottigliaDb(models.Model):
    codigo = models.CharField(max_length = 50,unique=True)
    nombre = models.CharField(max_length = 50)
    entrada = models.IntegerField()
    salida = models.IntegerField()
    stock = models.IntegerField()
    pCompra = models.FloatField()
    pVenta = models.FloatField()



    TIPO_CHOICES = [
        ('VINOMALBEC' , 'Vino Malbec'),
        ('VINOBLANCO' , 'Vino Blanco'),
        ('VINOBLEND' , 'Vino Blend'),
        ('VINOCABERNET' , 'Vino Cavernet'),
        ('CHAMPANGNE' , 'Champagne'),
        ('RON' , 'Ron'),
        ('WHISKY' , 'Whisky'),
        ('APERITIVO' , 'Aperitivo'),
        ('GIN' , 'Gin'),
        ('CERVEZA' , 'Cerveza'),
        ('CRISTALERIA' , 'Cristaleria'),
        ('TEQUILA','Tequila'),
        ('VODKA' , 'Vodka'),
        ('GASEOSA' , 'Gaseosa'),
        ('JUGOS' , 'Jugos'),
        ('SNACKS' , 'Snacks'),
        ('OTRO' , 'Otro'),
    ]
    tipo = models.CharField(max_length = 15,
    choices=TIPO_CHOICES,
    default='OTRO',
    )
    img = models.ImageField(upload_to='productos',blank=True)
    def __str__(self):
        return '{}-{}'.format(self.nombre,self.tipo) #cambiamos los nombres en el admin panel
    
    
class Avatar(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
        github = models.URLField(max_length=200,null=True,blank=True)
        descripcion = models.CharField(max_length=200,null=True,blank=True)
