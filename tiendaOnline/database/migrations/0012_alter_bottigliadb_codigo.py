# Generated by Django 4.1.2 on 2022-11-30 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_alter_bottigliadb_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottigliadb',
            name='codigo',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]