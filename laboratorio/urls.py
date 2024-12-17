from django.urls import path
from . import views

urlpatterns = [
    # path('', views.laboratorio, name='laboratorio'),
    path('', views.index, name='index'),
    path('listado-laboratorios/', views.listar_laboratorios, name="listar_laboratorios"),
    path('listado-laboratorios/eliminar/<int:laboratorio_id>', views.eliminar_laboratorio, name="eliminar_laboratorio"),
    path('listado-laboratorios/actualizar/<int:laboratorio_id>', views.actualizar_laboratorio, name="actualizar_laboratorio"),
    path('listado-laboratorios/agregar/', views.agregar_laboratorio, name="agregar_laboratorio"),
    
]
