from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from ..models.course import Course

# from ..models.purchased_course import PurchasedCourse
from django.contrib import messages
from django.shortcuts import redirect


@method_decorator(login_required(login_url="login"), name="dispatch")
class AccountCourseDelete(DeleteView):
    model = Course
    template_name = "pages/account-courses.html"
    success_url = reverse_lazy("account_courses")

    def form_valid(self, form):
        self.object = self.get_object()

        if self.object.purchasedcourse_set.exists():
            messages.error(
                self.request, "Nie można usunąć kursu, który był już zakupiony"
            )
            return redirect("account_courses")
        else:
            response = super().form_valid(form)
            messages.success(self.request, "Kurs został usunięty")
            return response
