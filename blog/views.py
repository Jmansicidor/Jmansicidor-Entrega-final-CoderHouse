from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
import blog
from blog.forms import UserForms
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
# Create your views here.
from blog.models import Create


class blog_new(LoginRequiredMixin, CreateView):
    model = Create
    success_url = reverse_lazy("bloginicio")
    fields = ["user", "theme", "text_area"]


class blog_edit(LoginRequiredMixin, UpdateView):
    model = Create
    success_url = reverse_lazy("bloginicio")
    fields = ["user", "theme", "text_area"]


class blog_list(ListView):
    model = Create
    template_name = "blog/blog_list.html"


class blog_detail(DetailView):
    model = Create
    template_name = "blog/blog_detail.html"


class blog_delete(LoginRequiredMixin, DeleteView):
    model = Create
    success_url = reverse_lazy("bloginicio")
