from django import forms
from .models import Materia

class AddMateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ('codigo', 'nombre', 'descripcion', 'docente', 'estado')
        labels = {
            'codigo': 'Codigo Materia',
            'nombre': 'Nombre Materia',
            'descripcion': 'Descripcion Materia',
            'docente': 'Docente a cargo',
            'estado': 'Estado de la Materia',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'docente': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

class EditMateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ('codigo', 'nombre', 'descripcion', 'docente', 'estado')
        labels = {
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'docente': 'Docente',
            'estado': 'Estado',
        }
        widgets = {
            
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_original'}),
            'nombre': forms.TextInput(attrs={'type': 'text', 'id': 'nombre_editar'}),
            'descripcion': forms.TextInput(attrs={'type': 'text', 'id': 'descripcion_editar'}),
            'docente': forms.Select(attrs={'class': 'form-control', 'id': 'docente_editar'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'estado_editar'}),
        }