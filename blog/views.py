from django.shortcuts import render, redirect
from blog.forms import UserForms


# Create your views here.


def blog_new(request):
    if request.method == 'POST':
        formnewBlog = UserForms(request.POST)
        if formnewBlog.is_valid():
            formnewBlog.save()
            return redirect("index")
    else:
        formnewBlog = UserForms()
    return render(request, "blog/blog_create.html", {"formnewBlog": formnewBlog})
