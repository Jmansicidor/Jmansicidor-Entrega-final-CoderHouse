from django.contrib import admin
from blog.models import Create
from usuarios.models import*


# Register your models here.


admin.site.register(User)
admin.site.register(Create)
