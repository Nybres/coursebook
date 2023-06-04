from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"foo": "ładunek"}
    return render(request, "pages/index.html", context)