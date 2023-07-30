from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..helpers import check_membership


@login_required(login_url="login")
def AccountView(request):
    user = request.user
    isMember = check_membership(user)
    context = {
        "user": user,
        "isMember": isMember,
    }

    return render(request, "pages/account.html", context)
