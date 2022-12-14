# Generated by Django 4.1.2 on 2022-11-08 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_bottigliadb_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottigliadb',
            name='tipo',
            field=models.CharField(choices=[('VM', 'Vino Malbec'), ('VB', 'Vino Blanco'), ('VBLEND', 'Vino Blend'), ('VC', 'Vino Cavernet'), ('CH', 'Champagne'), ('RON', 'Ron'), ('WH', 'Whisky'), ('AP', 'Aperitivo'), ('GIN', 'Gin'), ('CER', 'Cerveza'), ('CR', 'Cristaleria'), ('TE', 'Tequila'), ('VK', 'Vodka'), ('GA', 'Gaseosa'), ('JU', 'Jugos'), ('SN', 'Snacks'), ('OTRO', 'Otro')], default='OTRO', max_length=15),
        ),
    ]
