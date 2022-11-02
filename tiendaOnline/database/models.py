from django.db import models

# Create your models here.
class bottigliaDb(models.Model):
    codigo = models.CharField(max_length = 50)
    nombre = models.CharField(max_length = 50)
    entrada = models.IntegerField()
    salida = models.IntegerField()
    stock = models.IntegerField()
    pCompra = models.FloatField()
    pVenta = models.FloatField()

    VINOMALBEC = 'VM'
    VINOBLANCO = 'VB'
    VINOBLEND = 'VBLEND'
    VINOCABERNET = 'VC'
    CHAMPANGNE = 'CH'
    RON = 'RON'
    WHISKY = 'WH'
    APERITIVO = 'AP'
    GIN = 'GIN'
    CERVEZA = 'CER'
    CRISTALERIA = 'CR'
    VODKA = 'VK'
    GASEOSA = 'GA'
    JUGOS = 'JU'
    SNACKS = 'SN'
    OTRO = 'OTRO'

    TIPO_CHOICES = [
        (VINOMALBEC , 'Vino Malbec'),
        (VINOBLANCO , 'Vino Blanco'),
        (VINOBLEND , 'Vino Blend'),
        (VINOCABERNET , 'Vino Cavernet'),
        (CHAMPANGNE , 'Champagne'),
        (RON , 'Ron'),
        (WHISKY , 'Whisky'),
        (APERITIVO , 'Aperitivo'),
        (GIN , 'Gin'),
        (CERVEZA , 'Cerveza'),
        (CRISTALERIA , 'Cristaleria'),
        (VODKA , 'Vodka'),
        (GASEOSA , 'Gaseosa'),
        (JUGOS , 'Jugos'),
        (SNACKS , 'Snacks'),
        (OTRO , 'Otro'),
    ]
    tipo = models.CharField(max_length = 15,
    choices=TIPO_CHOICES,
    default=OTRO,
    )
    