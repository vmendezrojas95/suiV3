from django.db import models

# Create your models here.
class Materia(models.Model):
    codigo = models.CharField(max_length=10, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=200)
    docente = models.ForeignKey('docente.Docente', null=False, blank=False, on_delete=models.DO_NOTHING)
    estado = models.BooleanField(default=True)

    def __str__(self):
      return '{} - {} - docente: {}'.format(self.codigo, self.nombre, self.docente)


    '''def delete(self, *args):
        self.estado = False
        self.save()
        return True
        '''
    # Cambia el estado a False de la materia, no la elimina!