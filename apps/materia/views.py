from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddMateriaForm, EditMateriaForm
from django.contrib import messages
from .models import Materia
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class MateriaView(LoginRequiredMixin,View):
    def get(self, request):
        materias = Materia.objects.all()
        form_materia = AddMateriaForm()
        form_editar = EditMateriaForm()
        context = {
            'materias': materias,
            'form_materia': form_materia,
            'form_editar': form_editar,
        }
        return render(request, 'materia.html', context)

class AddMateriaView(LoginRequiredMixin,View):
    def post(self, request):
        print("Guardar materia")
        if request.method == 'POST':
            form_materia = AddMateriaForm(request.POST, request.FILES)
            if form_materia.is_valid():
                try:
                    form_materia.save()
                except:
                    messages(request, 'Error al guardar la materia')
                    return redirect('materia')
        return redirect('materia')

class EditMateriaView(LoginRequiredMixin, View):
    def post(self, request):
        print("Editar materia")
        if request.POST:
            codigo_original = request.POST.get('codigo_editar')
            print("Código de la materia:", codigo_original)
            materia = Materia.objects.get(codigo=codigo_original)
            print("Materia a editar:", materia)
            form_editar = EditMateriaForm(request.POST, instance=materia)
            print("Formulario:", form_editar)
            if form_editar.is_valid():
                try:
                    print("Formulario válido")
                    form_editar.save()
                    print("Materia editada")
                    return redirect('materia')
                except:
                    messages(request, 'Error al editar la materia')
                    return redirect('materia')

class DeleteMateriaView(LoginRequiredMixin, View):
    def post(self, request):
        print("Eliminar materia")
        if request.POST:
            codigo = request.POST.get('id_materia')
            print("Código de la materia:", codigo)
            try:
                materia = Materia.objects.get(codigo=codigo)
                print("Materia encontrada:", materia)
                materia.delete()
                print("Materia eliminada")
                print("Materia:", materia)
                return redirect('materia')
            except Materia.DoesNotExist:
                print("Materia no encontrada")
                return redirect('materia')
        else:
            print("No se recibió una solicitud POST")
        return redirect('materia')
