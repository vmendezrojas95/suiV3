from django.urls import path
from .views import MateriaView, AddMateriaView, EditMateriaView, DeleteMateriaView

urlpatterns = [
    path('', MateriaView.as_view(), name='materia'),
    path('add_materia', AddMateriaView.as_view(), name='AddMateria'),
    path('edit_materia', EditMateriaView.as_view(), name='EditMateria'),
    path('delete_materia', DeleteMateriaView.as_view(), name='DeleteMateria'),
    
]
