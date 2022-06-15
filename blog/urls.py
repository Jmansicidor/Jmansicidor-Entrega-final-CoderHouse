from django.urls import path
from blog.views import blog_new

urlpatterns = [
    path('blog_new', blog_new)
]
