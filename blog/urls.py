from django.urls import path
from blog import views


urlpatterns = [
    path('blog_new/', views.blog_new.as_view(), name="blogcrear"),
    path('', views.blog_list.as_view(), name="bloginicio"),
    path('blog_detail/<pk>/', views.blog_detail.as_view(), name="blogdetalle"),
    path('blog_edit/<pk>/', views.blog_edit.as_view(), name="blog_update"),
    path('blog_delete/<pk>', views.blog_delete.as_view(), name="blog_delete"),

]
