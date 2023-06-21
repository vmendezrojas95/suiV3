from django.db import models
from apps.carrera.models import Carrera


# Create your models here.
class Estudiante(models.Model):
    dni = models.CharField(max_length=8)
    legajo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    carrera = models.ForeignKey('carrera.Carrera', null=False, blank=False, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    sexo = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')))
    # La matricula se tiene que activar
    

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)

   # def delete(self, *args):
    #    self.estado = False
     #   self.save()
      #  return True