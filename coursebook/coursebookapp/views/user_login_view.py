from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.contrib import messages


class UserLoginView(LoginView):
    template_name = "pages/login.html"

    def form_invalid(self, form):
        messages.error(self.request, "Nieprawidłowy login lub hasło")
        return super().form_invalid(form)

    def get_success_url(self):
        if self.request.user.is_authenticated:
            messages.success(self.request, "Zostałeś zalogowany")
            return reverse_lazy("account")
        else:
            return reverse_lazy("login")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("account"))
        return super().dispatch(request, *args, **kwargs)
