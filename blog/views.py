from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView

from blog.forms import UserForms
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
# Create your views here.
from blog.models import Create, Profile


class blog_new(LoginRequiredMixin, CreateView):
    model = Create
    success_url = reverse_lazy("bloginicio")
    fields = ["theme", "text_area"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class blog_profile(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("bloginicio")
    fields = ["user", "image"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class blog_edit(LoginRequiredMixin, UpdateView):
    model = Create
    success_url = reverse_lazy("bloginicio")
    fields = ["theme", "text_area"]


class blog_list(ListView):
    model = Create
    template_name = "blog/blog_list.html"


class blog_detail(DetailView):
    model = Create
    template_name = "blog/blog_detail.html"


class blog_delete(LoginRequiredMixin, DeleteView):
    model = Create
    success_url = reverse_lazy("bloginicio")


def userprofile(request):
    userimgprofile = Profile.objects.count()
    return render(request, "bloginicio", {"userimgprofile": userimgprofile})
