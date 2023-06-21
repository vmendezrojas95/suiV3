from django.db import models
from apps.estudiante.models import Estudiante
from apps.materia.models import Materia


# Create your models here.

class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.estudiante, self.materia, self.fecha)
    