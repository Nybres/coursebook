from django.shortcuts import render


def HomeView(request):
    context = {"foo": "home"}
    return render(request, "pages/index.html", context)
