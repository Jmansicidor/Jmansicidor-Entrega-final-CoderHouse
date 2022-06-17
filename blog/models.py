from django.db import models

# Create your models here.
from usuarios.models import UserInfo


class Avatar(models.Model):
    pass


class Create(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, null=True)
    theme = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    text_area = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.user.name} {self.theme} {self.date} {self.text_area}  "
