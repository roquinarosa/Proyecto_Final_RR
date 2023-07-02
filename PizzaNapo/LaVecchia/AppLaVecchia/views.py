from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "AppLaVecchia/index.html")

def menu(request):
    return render(request, "LaVecchia/menu.html")

def proveedores(request):
    return render(request, "LaVecchia/proveedores.html")

def clientes(request):
    return render(request, "LaVecchia/clientes.html")


def empleados(request):
    return render(request, "LaVecchia/empleados.html")
