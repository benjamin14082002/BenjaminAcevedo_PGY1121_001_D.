from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, nombreUsuario, password, tipoUsuario='cliente'):
        if not nombreUsuario:
            raise ValueError('El nombre de usuario debe ser establecido')
        user = self.model(
            nombreUsuario=nombreUsuario,
            tipoUsuario=tipoUsuario,
        )
        user.set_password(password)  # Utiliza contraseña para establecer la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, nombreUsuario, password):
        user = self.create_user(
            nombreUsuario=nombreUsuario,
            password=password,  # Usa contraseña aquí
            tipoUsuario='admin',
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    ADMIN = 'admin'
    CLIENTE = 'cliente'
    
    TIPO_USUARIO_CHOICES = [
        (ADMIN, 'Admin'),
        (CLIENTE, 'Cliente'),
    ]

    nombreUsuario = models.CharField(max_length=100, unique=True, verbose_name='Nombre de Usuario')
    tipoUsuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES, default=CLIENTE, verbose_name='Tipo de Usuario')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'nombreUsuario'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nombreUsuario

    def has_perm(self, perm, obj=None):
        # En un modelo personalizado, se puede asumir que todos los usuarios tienen permiso para todo
        return True

    def has_module_perms(self, app_label):
        # En un modelo personalizado, se puede asumir que todos los usuarios tienen permiso para todos los módulos
        return True



class Medico(models.Model):
    nombre = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.fecha} - {self.hora_inicio} a {self.hora_fin}"

class Reserva(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reserva de {self.medico.nombre} el {self.fecha_reserva}"
