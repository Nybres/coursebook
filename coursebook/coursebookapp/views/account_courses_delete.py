from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from ..models.course import Course
from django.contrib import messages

@method_decorator(login_required(login_url="login"), name="dispatch")
class AccountCourseDelete(DeleteView):
    model = Course
    template_name = "pages/account-courses.html"
    success_url = reverse_lazy("account_courses")

    def form_valid(self, form):
        # Get the object being deleted
        self.object = self.get_object()
        # Call the delete() method from the parent class to handle standard deletion logic
        response = super().form_valid(form)
        # Add your custom logic here, such as displaying a success message
        messages.success(self.request, "Kurs został usunięty")
        return response
