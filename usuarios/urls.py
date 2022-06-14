from unicodedata import name
from django.urls import path
from usuarios import views

urlpatterns = [
    path("", views.users, name="users"),
    path('crear/', views.SingUpView.as_view(), name = 'user_singup' ),
    path('actualizar/', views.SingUpdateView.as_view(), name = 'user_update' ),
]
