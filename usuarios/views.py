from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserForms
from .models import User


# Create your views here.
def users(request):
    formaUser = User.objects.all()
    return render(request, "list.html", {"userslist": formaUser})
