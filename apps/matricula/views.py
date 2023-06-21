from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Matricula
from .forms import MatriculaForm

class MatriculaView(LoginRequiredMixin, View):
    print('MatriculaView')
    def get(self, request):
        matriculas_activos = Matricula.objects.filter(estudiante__estado=True)
        matriculas_inactivos = Matricula.objects.filter(estudiante__estado=False)
        context = {
            'matriculas_activos': matriculas_activos,
            'matriculas_inactivos': matriculas_inactivos,
        }
        
        print('Matriculas activos:', matriculas_activos)
        print('Matriculas inactivos:', matriculas_inactivos)

        return render(request, 'matricula.html', context)

class CrearMatriculaView(LoginRequiredMixin, View):
    def get(self, request):
        form = MatriculaForm()
        context = {
            'form': form,
        }
        return render(request, 'crear_matricula.html', context)

    def post(self, request):
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matricula')
        context = {
            'form': form,
        }
        return render(request, 'crear_matricula.html', context)