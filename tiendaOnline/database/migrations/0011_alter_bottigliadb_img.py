# Generated by Django 4.1.2 on 2022-11-28 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_alter_bottigliadb_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottigliadb',
            name='img',
            field=models.ImageField(blank=True, upload_to='productos'),
        ),
    ]
