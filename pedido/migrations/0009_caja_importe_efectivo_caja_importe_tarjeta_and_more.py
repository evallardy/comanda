# Generated by Django 4.0.4 on 2023-10-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0008_alter_caja_estatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='caja',
            name='importe_efectivo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Importe'),
        ),
        migrations.AddField(
            model_name='caja',
            name='importe_tarjeta',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Importe'),
        ),
        migrations.AddField(
            model_name='caja',
            name='importe_tranferencia',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Importe'),
        ),
    ]
