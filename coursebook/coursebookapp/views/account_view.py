from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def AccountView(request):
    user = request.user
    return render(request, "pages/account.html", {"user": user})
