from django.contrib import admin

# Register your models here.
from usuarios.models import User
from usuarios.models import Avatar


admin.site.register(User)
admin.site.register(Avatar)