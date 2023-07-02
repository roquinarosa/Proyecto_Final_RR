from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Menu
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

class MenuListView(ListView):
    model = Menu
    template_name = "AppLaVecchia/class_list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class MenuDetailView(LoginRequiredMixin, DetailView):
    model = Menu
    template_name = "AppLaVecchia/class_detail.html"

    # login_url = '/users/login/'

    # def get_login_url(self):
    #     return self.login_url


class MenuCreateView(CreateView):
    

    model = Menu
    template_name = "AppLaVecchia/class_create.html"
    fields = ["nombre", "precio"]

   
    success_url = reverse_lazy("Menu")


class MenuUpdateView(UpdateView):
    model = Menu
    success_url = reverse_lazy("List")
    fields = ["id", "nombre", "precio"]
    template_name = "AppLaVecchia/class_update.html"


class MenuDeleteView(DeleteView):
    model = Menu
    success_url = reverse_lazy("List")
    template_name = 'AppLaVecchia/class_confirm_delete.html'