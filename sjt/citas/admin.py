from django.contrib import admin
from citas.models import *

class PacienteAdmin(admin.ModelAdmin):
    pass

class MedicoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Medico, MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)
