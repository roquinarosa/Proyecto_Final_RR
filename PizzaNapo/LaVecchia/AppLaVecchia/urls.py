from django.urls import path 
from AppLaVecchia import views

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('menu/', views.menu, name="Menu"),
    path('proveedores/', views.proveedores, name="Proveedores"),
    path('clientes/', views.clientes, name="Clientes"),
    path('empleados/', views.empleados, name="Empleados"),
    path('menu-formulario/', views.menu_formulario, name="Formulario_Menu"),
    path('busca-menu-formulario/', views.buscar_menu_formulario, name="Buscar_Menu"),
    path('mostrar-menu/', views.mostrar_menu, name="Mostrar_Menu"),
    path('confirmar-borrado-menu/<id>/', views.menu_2, name="Borrar Menu"),


  
]