from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seeds/', views.seeds, name='seeds'),
    path('beds/', views.beds, name='beds'),
    path('planting/', views.planting, name='planting'),
]