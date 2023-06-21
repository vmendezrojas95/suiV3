'''from django.urls import path, include
from .views import carrera_view


urlspatterns = [
    path('carrera/', carrera_view, name='carrera'),

]
'''

from django.urls import path
from .views import CarreraView, AddCarreraView, EditCarreraView, DeleteCarreraView

#app_name = 'carrera'

urlpatterns = [
    path('', CarreraView.as_view(), name='carrera'),
    path('add_carrera', AddCarreraView.as_view(), name='AddCarrera'),
    path('edit_carrera', EditCarreraView.as_view(), name='EditCarrera'),
    path('delete_carrera', DeleteCarreraView.as_view(), name='DeleteCarrera'),
]


