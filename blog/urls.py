from django.urls import path
from blog import views
from blog.views import blog_delete

urlpatterns = [
    path('blog/', views.blog_new.as_view(), name="blogcrear"),
    path('blog_list', views.blog_list.as_view(), name="bloginicio"),
    path('blog_detail/<pk>/', views.blog_detail.as_view(), name="blogdetalle"),
    path('blog_edit/<pk>/', views.blog_edit.as_view(), name="blog_update"),
    path('blog_delete/<int:id>', blog_delete, name="blog_delete")

]
