from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo = models.CharField(max_length=10)
    # Mostrar los estudiantes disponibles para la carrera
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    duracion = models.PositiveSmallIntegerField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '{}' ' - ' 'duracion(Años): {} '.format( self.nombre, self.duracion)
    
    

   # def delete(self, *args):
    #    self.estado = False
     #   self.save()
      #  return True