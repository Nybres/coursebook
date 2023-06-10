from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def AccountView(request):
    user = request.user
    print(user)
    return render(request, "pages/account.html", {"user": user})
