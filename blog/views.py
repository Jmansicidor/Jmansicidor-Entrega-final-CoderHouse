from django.shortcuts import render, redirect, get_object_or_404

import blog
from blog.forms import UserForms

# Create your views here.
from blog.models import Create


def blog_new(request):
    if request.method == 'POST':
        formnewBlog = UserForms(request.POST)
        if formnewBlog.is_valid():
            formnewBlog.save()
            return redirect("bloginicio")
    else:
        formnewBlog = UserForms()
    return render(request, "blog/blog_create.html", {"formnewBlog": formnewBlog})


def blog_edit(request, id):
    if request.method == 'POST':
        formnewBlog = UserForms(request.POST)
        if formnewBlog.is_valid():
            formnewBlog.save()
            return redirect("bloginicio")
    else:
        blog = get_object_or_404(Create, pk=id)
        formnewBlog = UserForms(instance=blog)
    return render(request, "blog/blog_edit.html", {"formnewBlog": formnewBlog})


def blog_list(request):
    formaBlog = Create.objects.all()
    return render(request, "blog/blog_list.html", {"bloglist": formaBlog})


def blog_detail(request, id):
    blog = Create.objects.get(pk=id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})


def blog_delete(request, id):
    blog = get_object_or_404(Create, pk=id)
    if blog:  # \\si persona exite  elimine
        blog.delete()
    return redirect('bloginicio')
