from django.contrib import admin
from .models import Medico, Horario, Reserva,Usuario

# Registrar los modelos para que sean administrables desde el panel de administración
admin.site.register(Medico)
admin.site.register(Horario)
admin.site.register(Reserva)
admin.site.register(Usuario)
