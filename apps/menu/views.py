from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def menu_view(request):
    return render(request, 'menu.html')

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def products_view(request):
    return render(request, 'products.html')

def exit_view(request):
    logout(request)
    return render(request, 'registration/login.html')
