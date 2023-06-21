from django.urls import path
from .views import docente_view

urlpatterns = [
   path('', docente_view, name='docente')
]