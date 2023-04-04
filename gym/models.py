from django.db import models

# Create your models here.
class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.EmailField()
    pase = models.CharField(max_length=30)
    documento = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Correo: {self.correo} - Pase: {self.pase} - Documento: {self.documento}'


class Profesores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.EmailField()
    documento = models.IntegerField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Correo: {self.correo} - DNI: {self.documento}'


class Clases(models.Model):
    nombre = models.CharField(max_length=40)
    profesor = models.CharField(max_length=40)
    dias = models.CharField(max_length=40)
    horario = models.CharField(max_length=40)

    def __str__(self):
        return f'Nombre:{self.nombre} - Profesor: {self.profesor} - Dias: {self.dias} - Horario: {self.horario}'
