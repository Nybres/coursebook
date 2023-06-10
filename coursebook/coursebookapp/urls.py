from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView, name="home"),
    path("login", views.LoginView.as_view(), name="login"),
    path("register-customer", views.RegisterView.as_view(), name="register_customer"),
    path("register-company", views.RegisterView.as_view(), name="register_company"),
    path("account", views.AccountView, name="account"),
]
