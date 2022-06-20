from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from usuarios import views

urlpatterns = [
    path("", views.users, name="users"),
    path('login/', views.SingUpView.as_view(), name='user_singin'),
    path('update/<pk>', views.SingUpdateView.as_view(), name='user_update'),
    path('detail/<pk>', views.SingDetail.as_view(), name='user_detail'),
    path("ingresar/", views.UserLogin.as_view(), name="user_login"),
    path('agregarAvatar', views.agregarAvatar, name="agregarAvatar"),
    path("salir/", views.UserLogOut.as_view(), name="user_logout"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)