from django.db import models

# Create your models here.
class Docente(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    estado = models.BooleanField(default=True)
    sexo = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')))

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)

    def delete(self, *args):
        self.estado = False
        self.save()
        return True