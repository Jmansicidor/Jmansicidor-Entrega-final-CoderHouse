from curses.ascii import US
from distutils.command.upload import upload
from django.contrib.auth.models import User
from unicodedata import name
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from django.db import models

user_sex = [
    (1, 'Hombre'),
    (2, 'Mujer'),
    (3, 'Otro')
]


class UserInfo(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_sex = models.IntegerField(
        null=False, blank=False,
        choices=user_sex
    )
    mailbox = models.CharField(max_length=255)

    def __str__(self):
        return f'User {self.id}: {self.name} {self.last_name} {self.mailbox}'


# clase para agregar avatar al usuario

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatar', null=True, blank = True)
