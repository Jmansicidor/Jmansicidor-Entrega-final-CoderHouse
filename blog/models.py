from django.db import models

# Create your models here.
from usuarios.models import UserInfo
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="defaultimage.png")

    def __str__(self):
        return f'Perfil de {self.user.username}'


class Create(models.Model):
    theme = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    text_area = models.TextField(max_length=500)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return f" {self.theme} {self.date} {self.text_area}  "
