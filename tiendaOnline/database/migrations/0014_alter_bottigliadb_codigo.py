# Generated by Django 4.1.2 on 2022-12-01 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_empleados_fechainsercion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottigliadb',
            name='codigo',
            field=models.CharField(max_length=50),
        ),
    ]