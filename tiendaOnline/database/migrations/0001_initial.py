# Generated by Django 4.1.2 on 2022-11-02 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bottigliaDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('entrada', models.IntegerField()),
                ('salida', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('pCompra', models.FloatField()),
                ('pVenta', models.FloatField()),
                ('tipo', models.CharField(choices=[('VM', 'Vino Malbec'), ('VB', 'Vino Blanco'), ('VBLEND', 'Vino Blend'), ('VC', 'Vino Cavernet'), ('CH', 'Champagne'), ('RON', 'Ron'), ('WH', 'Whisky'), ('AP', 'Aperitivo'), ('GIN', 'Gin'), ('CER', 'Cerveza'), ('CR', 'Cristaleria'), ('VK', 'Vodka'), ('GA', 'Gaseosa'), ('JU', 'Jugos'), ('SN', 'Snacks'), ('OTRO', 'Otro')], default='OTRO', max_length=15)),
            ],
        ),
    ]
