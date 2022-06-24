from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from .models import UserInfo, Avatar
from .forms import AvatarFormulario
from django.contrib.auth.decorators import login_required


# Create your views here.
def users(request):
    formaUser = UserInfo.objects.all()
    return render(request, "list.html", {"userslist": formaUser})


class SingUpView(SuccessMessageMixin, CreateView):
    template_name = 'user_create_count.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('user_login')
    success_message = 'Se ha creado su cuenta sastifactoriamente'


class SingDetail(DetailView):
    model = User
    template_name = 'user_detail.html'


class SingUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "user_updete_count.html"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
        return reverse_lazy("user_detail", kwargs={"pk": self.request.user.id})


class UserLogin(LoginView):
    template_name = 'user_login.html'
    next_page = reverse_lazy("users")
  
class UserLogOut(LogoutView):
    template_name = 'user_logout.html'
    next_page = reverse_lazy("bloginicio")

@login_required
def agregarAvatar(request):

    if request.method == 'POST':

        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            u = User.objects.get(username=request.user)

            avatar = Avatar(user = u, image=miFormulario.cleaned_data['image'])

            avatar.save()

            return render(request, 'list.html')

    else:

        miFormulario = AvatarFormulario()

    return render(request, "agregarAvatar.html", {"miFormulario":miFormulario})
