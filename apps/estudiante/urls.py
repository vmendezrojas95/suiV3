from django.urls import path
from .views import EstudianteView, AddEstudianteView, EditEstudianteView, DeleteEstudianteView, DatosEstudianteView,DetalleEstudianteView


urlpatterns = [
    path('', EstudianteView.as_view(), name='estudiante'),
    path('add_estudiante', AddEstudianteView.as_view(), name='agregar_estudiante'),
    path('edit_estudiante', EditEstudianteView.as_view(), name='editar_estudiante'),
    path('del_estudiante', DeleteEstudianteView.as_view(), name='eliminar_estudiante'),
    path('estudiante', DatosEstudianteView.as_view(), name='datos_estudiantes'),
    path('estudiante/<str:legajo>', DetalleEstudianteView.as_view(), name='detalle_estudiante'),
]
