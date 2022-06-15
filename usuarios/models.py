from curses.ascii import US
from distutils.command.upload import upload
from email.mime import image
import mailbox
from pickle import TRUE

from unicodedata import name
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.db import models

user_sex = [
    (1, 'Hombre'),
    (2, 'Mujer'),
    (3, 'Otro')
]


class User(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_sex = models.IntegerField(
        null=False, blank=False,
        choices=user_sex
    )
    mailbox = models.CharField(max_length=255)

    def __str__(self):
        return f'User {self.id}: {self.name} {self.last_name} {self.mailbox}'


class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    passsword1 = forms.CharField(label='contraseña', widget = forms.PasswordInput)
    password2: forms.CharField(label='repetir contraseña', widget = forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','password1','password2']
        



class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'avatar', null = True)
   