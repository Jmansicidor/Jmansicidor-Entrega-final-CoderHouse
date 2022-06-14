from curses.ascii import US
import mailbox

from unicodedata import name
from django import forms
from django.contrib.auth.forms import UserCreationForm

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
        fields = ['name','email','password1','password2']
        