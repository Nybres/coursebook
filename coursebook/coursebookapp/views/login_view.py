from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.contrib import messages


class LoginView(LoginView):
    template_name = "pages/login.html"

    def form_invalid(self, form):
        messages.error(self.request, "Nieprawidłowy login lub hasło")
        return super().form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "Pomyślnie zalogowano")
        return reverse_lazy("account")
