from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    class Meta:
        db_table = 'Usuario'

        permissions = (
    # Cambio contraseña
            ('cambio_contrasena', 'Cambio de contraseña'),
            ('servicio_bar', 'Servicio de bar'),
            ('servicio_cocina', 'Servicio de cocina'),
            ('servicio_atencion', 'Servicio de atención'),
            ('catalogos', 'Catálogos'),
            ('usuarios', 'Usuarios'),
            ('reportes_ejecutivos', 'Reportes ejecutivos'),
        )   