from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login", views.login, name="login"),
    path("register-customer", views.register_customer, name="register_customer"),
    path("register-company", views.register_company, name="register_company"),
]
