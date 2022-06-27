from django.contrib import admin
from blog.models import Create,Profile
from usuarios.models import*


# Register your models here.


admin.site.register(UserInfo)
admin.site.register(Create)
admin.site.register(Avatar)
admin.site.register(Profile)

