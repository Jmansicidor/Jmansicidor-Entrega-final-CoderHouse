from django.urls import path
from blog.views import blog_new, blog_list, blog_detail, blog_edit, blog_delete

urlpatterns = [
    path('blog', blog_new,name="blogcrear"),
    path('blog_list', blog_list, name="bloginicio"),
    path('blog_detail/<int:id>', blog_detail),
    path('blog_edit/<int:id>', blog_edit),
    path('blog_delete/<int:id>', blog_delete)

]
