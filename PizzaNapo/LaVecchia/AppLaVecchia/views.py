from django.shortcuts import render
from .models import Menu
from AppLaVecchia.forms import MenuFormulario, BuscaMenuForm


# Create your views here.

def inicio(request):
    return render(request, "AppLaVecchia/index.html")

def menu(request):
    return render(request, "AppLaVecchia/menu.html")

def proveedores(request):
    return render(request, "AppLaVecchia/proveedores.html")

def clientes(request):
    return render(request, "AppLaVecchia/clientes.html")


def empleados(request):
    return render(request, "AppLaVecchia/empleados.html")


def menu_formulario(request):
    if request.method == "POST":
        miFormulario = MenuFormulario(request.POST) 

        print(miFormulario)
        
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            menu = Menu (nombre=informacion["menu"], precio=informacion["precio"])

            menu.save()

            return render(request, "AppLaVecchia/index.html")
        
    else:

        miFormulario = MenuFormulario()

    return render(request, "AppLaVecchia/menu_formulario.html", {"miFormulario": miFormulario})

def buscar_menu_formulario(request):

    if request.method == "GET":
       
        busqueda = request.GET.get('busqueda', '')   
        menus = Menu.objects.filter(nombre__icontains=busqueda)
        context = {'menus': menus}
        return render(request, 'AppLaVecchia/buscar_menu_formulario.html', context)
    

def mostrar_menu(request):

    menu = Menu.objects.all() #trae todos los menu

    contexto= {"menu":menu} 

    return render(request, "AppLaVecchia/mostrar_menu.html",contexto)

def menu_2(request, id):

    menu = Menu.objects.get(id=id)
    menu.delete()
 
    # vuelvo al menú
    menu = Menu.objects.all()  # trae todos los profesores
 
    contexto = {"menu": menu}
 
    return render(request, "AppLaVecchia/mostrar_menu.html", contexto)

