# Generated by Django 4.2.5 on 2023-09-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0006_detalle_nom_paquete_alter_detalle_nom_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle',
            name='especifico',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Especificación'),
        ),
    ]
