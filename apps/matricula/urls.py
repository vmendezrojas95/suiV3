from django.urls import path
from .views import MatriculaView

urlpatterns = [
    path('', MatriculaView.as_view(), name='matricula')
]