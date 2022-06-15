from unicodedata import name
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from usuarios import views

urlpatterns = [
    path("", views.users, name="users"),
    path('login/', views.SingUpView.as_view(), name = 'user_login' ),
    path('update/<pk>', views.SingUpdateView.as_view(), name = 'user_update' ),

]
