from django.urls import path
from .views import register, user_home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/login.html'), name='logout'),
    path('home/', user_home, name="user-home"),
]