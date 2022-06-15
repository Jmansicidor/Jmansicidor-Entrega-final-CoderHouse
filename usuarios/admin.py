from django.contrib import admin

# Register your models here.
from blog.models import Create
from usuarios.models import User

admin.site.register(User)
admin.site.register(Create)
