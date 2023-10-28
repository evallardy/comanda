# Generated by Django 4.0.4 on 2023-10-20 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loteria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sorteo',
            name='leido',
            field=models.IntegerField(choices=[(0, 'NO'), (1, 'SI')], default=0, verbose_name='Leído'),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='numero',
            field=models.IntegerField(default=0, verbose_name='Númnero sorteado'),
        ),
    ]
