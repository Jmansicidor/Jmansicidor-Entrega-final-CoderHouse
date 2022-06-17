from email.mime import image

from django import forms
from django.forms import ModelForm
from django.shortcuts import render
from usuarios.models import Avatar, UserInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

class UserForms(ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'
        widgets = {

        }

class AvatarFormulario(ModelForm):
    class Meta:
        model = Avatar
        fields = '__all__'
        widgets = {

        }
