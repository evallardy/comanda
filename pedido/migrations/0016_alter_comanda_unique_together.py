# Generated by Django 4.0.4 on 2023-10-27 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0015_caja_pago'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comanda',
            unique_together=set(),
        ),
    ]