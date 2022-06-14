from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .forms import UserForms
from .models import User


# Create your views here.
def users(request):
    formaUser = User.objects.all()
    return render(request, "list.html", {"userslist": formaUser})


class SingUpView(SuccessMessageMixin,CreateView):
    template_name = 'user_create_count.html'
    success_url = reverse_lazy('users')
    form_class = UserCreationForm 
    success_message = 'Se ha creado su cuenta sastifactoriamente'

class SingUpdateView(SuccessMessageMixin,UpdateView):
    template_name = 'user_updete_count.html'
    success_url = reverse_lazy('users')
    form_class = UserChangeForm
    success_message = 'Se han actualizados sus datos'