from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from Users.forms import UserEditForm, MyUserEditForm
from .forms import UserRegisterForm
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.urls import reverse_lazy
from .forms import CambiarPasswordForm


def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppLaVecchia/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppLaVecchia/index.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "AppLaVecchia/index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Users/login.html", {"form": form})


def register(request):

    if request.method == 'POST':

        
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppLaVecchia/index.html" ,  {"mensaje":"Usuario Creado :)"})

    else:
             
        form = UserRegisterForm()     

    return render(request,"Users/registro.html" ,  {"form":form})


    


@login_required
def editarPerfil(request):

    if request.method == 'POST':
        form = MyUserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = form(instance=request.user)
    
    context = {'form': form}
    return render(request, 'editar_perfil.html', context)

class CambiarPasswordView(LoginRequiredMixin, View):
    template_name = "users/cambiar_pass.html"
    form_class = CambiarPasswordForm
    success_url = reverse_lazy("Inicio")

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class})
    
    def post(self, request, *args, **kwargs):
        
        usuario = User.objects.get(id=request.user.id)
        form = self.form_class(request.POST)
        
        if form.is_valid():
            pass1 = form.cleaned_data.get("password1")
            pass2 = form.cleaned_data.get("password2")
        
            if pass1 == pass2:
                usuario.set_password(pass1)
                usuario.save()
                return render(request, "AppLaVecchia/index.html")
