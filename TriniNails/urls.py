from django.urls import path, include
from .views import home, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = {
    path("", home, name="home")
    path("login/", LoginView.as_view(template_name="TriniNails/login.html",name="login"))
    path("login/", LogoutView.as_view(template_name="TriniNails/logout.html",name="logout"))
    path("register/". register, name="register"),
    
}

