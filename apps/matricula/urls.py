from django.urls import path
from .views import MatriculaView, CrearMatriculaView

urlpatterns = [
    path('', MatriculaView.as_view(), name='matricula'),
    path('crear/', CrearMatriculaView.as_view(), name='crear_matricula'),
]