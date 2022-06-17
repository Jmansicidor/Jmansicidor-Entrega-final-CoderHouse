from django.contrib import admin
from blog.models import Create
from usuarios.models import*


# Register your models here.


admin.site.register(UserInfo)
admin.site.register(Create)
admin.site.register(Avatar)

