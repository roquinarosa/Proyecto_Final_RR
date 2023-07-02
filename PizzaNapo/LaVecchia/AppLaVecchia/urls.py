from django.urls import path 
from AppLaVecchia import views
from AppLaVecchia import class_views

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

# URL's basadas en clases
urlpatterns += [
    path('class-list/', class_views.MenuListView.as_view(), name="List"),
    path('class-detail/<pk>/', class_views.MenuDetailView.as_view(), name="Detail"),
    path('class-create/', class_views.MenuCreateView.as_view(), name="Create"),
    path('class-update/<pk>/', class_views.MenuUpdateView.as_view(), name="Update"),
    path('class-delete/<pk>/', class_views.MenuDeleteView.as_view(), name="Delete"),
]