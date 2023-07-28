from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inventory/', views.inventory, name='inventory'),
    path('basket/', views.basket, name='basket'),
    path('checkout/', views.checkout, name='checkout'),
]