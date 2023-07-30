from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("account")

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        messages.success(self.request, "Zostałeś wylogowany")
        return redirect(self.next_page)
