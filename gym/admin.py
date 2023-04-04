from django.contrib import admin
from .models import Estudiantes, Profesores, Clases

# Register your models here.
admin.site.register(Estudiantes)
admin.site.register(Profesores)
admin.site.register(Clases)