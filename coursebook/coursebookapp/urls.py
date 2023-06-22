from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView, name="home"),
    path("login", views.UserLoginView.as_view(), name="login"),
    path('logout', views.UserLogoutView.as_view(), name='logout'),
    path("register-customer", views.RegisterView.as_view(), name="register_customer"),
    path("register-company", views.RegisterView.as_view(), name="register_company"),
    # account
    path("account", views.AccountView, name="account"),
    path("account-courses", views.AccountCoursesView, name="account_courses"),
    path("account-instructors", views.AccountInstructorsView.as_view(), name="account_instructors"),
]
