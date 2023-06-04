from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"foo": "ładunek"}
    return render(request, "pages/index.html", context)


def login(request):
    context = {"foo": "ładunek"}
    return render(request, "pages/login.html", context)


def register_customer(request):
    context = {"foo": "ładunek"}
    return render(request, "pages/register-customer.html", context)


def register_company(request):
    context = {"foo": "ładunek"}
    return render(request, "pages/register-company.html", context)
