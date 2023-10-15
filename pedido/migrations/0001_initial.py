# Generated by Django 4.0.4 on 2023-09-04 21:27

import django.contrib.auth.mixins
from django.db import migrations, models
import django.db.models.deletion
import pedido.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripción')),
                ('cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('precio_unitario', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio unitario')),
                ('importe', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Importe')),
                ('estatus', models.IntegerField(choices=[(0, 'Cancelado'), (1, 'Solicitado'), (2, 'Elaborado'), (3, 'Entregado'), (4, 'Pagado'), (5, 'Cancelado elaborado'), (6, 'Cancelado difinitivo')], default=1, verbose_name='Estatus')),
                ('descripcion_cancela', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripción')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')),
                ('fecha_alta', models.DateTimeField(auto_now_add=True, verbose_name='Fecha alta')),
            ],
            options={
                'verbose_name': 'Operación',
                'verbose_name_plural': 'Operaciones',
                'db_table': 'Caja',
                'ordering': ['comanda', '-fecha_alta'],
            },
            bases=(models.Model, django.contrib.auth.mixins.PermissionRequiredMixin),
        ),
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesa', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mesa')),
                ('observacion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Observación')),
                ('estatus', models.IntegerField(choices=[(0, 'Cancelado'), (1, 'Actva'), (2, 'Pre-pagada'), (3, 'Cerrada'), (4, 'Cerrada sin pagar')], default=1, verbose_name='Estatus')),
                ('fecha_contable', models.DateField(default=pedido.models.default_fecha_contable, verbose_name='Fecha Contable')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')),
                ('fecha_alta', models.DateTimeField(auto_now_add=True, verbose_name='Fecha alta')),
            ],
            options={
                'verbose_name': 'Comanda',
                'verbose_name_plural': 'Comandas',
                'db_table': 'Comanda',
                'ordering': ['-fecha_alta'],
            },
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_producto', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre')),
                ('nota', models.CharField(max_length=255, verbose_name='Observación')),
                ('especificacion', models.JSONField(blank=True, null=True, verbose_name='Detalle')),
                ('cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('precio_unitario', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio unitario')),
                ('importe', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Importe')),
                ('estatus', models.IntegerField(choices=[(0, 'Cancelado'), (1, 'Solicitado'), (2, 'Elaborado'), (3, 'Entregado'), (4, 'Pagado'), (5, 'Cancelado elaborado'), (6, 'Cancelado difinitivo')], default=1, verbose_name='Estatus')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')),
                ('fecha_alta', models.DateTimeField(auto_now_add=True, verbose_name='Fecha alta')),
                ('caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.caja', verbose_name='Caja')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Detalle',
                'verbose_name_plural': 'Detalles',
                'db_table': 'Detalle',
                'ordering': ['caja', '-fecha_alta'],
            },
            bases=(models.Model, django.contrib.auth.mixins.PermissionRequiredMixin),
        ),
    ]