from django.urls import path
from .views import (
    DocenteView,
    AddDocenteView,
    EditDocenteView,
    DeleteDocenteView,
    DatosDocenteView,
    DetalleDocenteView
)

urlpatterns = [
    path('', DocenteView.as_view(), name='docente'),
    path('docente/agregar/', AddDocenteView.as_view(), name='agregar_docente'),
    path('docente/editar/', EditDocenteView.as_view(), name='editar_docente'),
    path('docente/eliminar/', DeleteDocenteView.as_view(), name='eliminar_docente'),
    path('docente/datos/', DatosDocenteView.as_view(), name='datos_docentes'),
    path('docente/<str:dni>/', DetalleDocenteView.as_view(), name='detalle_docente'),
]
