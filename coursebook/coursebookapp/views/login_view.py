from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class LoginView(LoginView):
    template_name = "pages/login.html"

    def get_success_url(self):
        return reverse_lazy("account")
