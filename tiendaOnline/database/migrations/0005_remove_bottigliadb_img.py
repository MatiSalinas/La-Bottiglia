# Generated by Django 4.1.2 on 2022-11-09 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_alter_bottigliadb_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottigliadb',
            name='img',
        ),
    ]
