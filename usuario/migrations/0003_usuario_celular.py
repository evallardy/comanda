# Generated by Django 4.0.4 on 2023-06-01 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_usuario_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='celular',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
