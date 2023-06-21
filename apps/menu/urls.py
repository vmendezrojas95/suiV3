from django.urls import path, include
from .views import menu_view, home_view, products_view, exit_view

urlpatterns = [
    path('', menu_view, name='menu'),
    path('home/', home_view, name='home'),
    path('products/', products_view, name='products'),
    path('exit/', exit_view, name='exit'),
]