from django import forms
from .models import Carrera

class AddCarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ('codigo', 'nombre', 'descripcion', 'duracion', 'estado')
        labels = {
            'codigo': 'Codigo Carrera',
            'nombre': 'Nombre Carrera',
            'descripcion': 'Descripcion Carrera',
            'duracion': 'Duracion Carrera',
            'estado': 'Estado de la Carrera',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'duracion': forms.TextInput(attrs={'class': 'form-control'}),
            'docente': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

class EditCarreraForm(forms.ModelForm):
    duracion = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'duracion_editar'}))
    class Meta:
        model = Carrera
        fields = ('codigo', 'nombre', 'descripcion', 'duracion', 'estado')
        labels = {
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'duracion': 'Duracion',
            'estado': 'Estado',
        }
        widgets = {
            
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_original'}),
            'nombre': forms.TextInput(attrs={'type': 'text', 'id': 'nombre_editar'}),
            'descripcion': forms.TextInput(attrs={'type': 'text', 'id': 'descripcion_editar'}),
            #'duracion': forms.Select(attrs={'class': 'form-control', 'id': 'duracion_editar'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'estado_editar'}),
        }