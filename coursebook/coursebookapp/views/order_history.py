from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..helpers import check_membership
from rest_framework import generics
from django.core.paginator import Paginator

from ..models import OrderHistory


@method_decorator(login_required(login_url="login"), name="dispatch")
class UserOrderHistory(generics.ListAPIView):
    template_name = "pages/order-history.html"
    default_pagination_size = 8

    def get(self, request, *args, **kwargs):
        user = request.user
        isMember = check_membership(user)

        last_orders = OrderHistory.objects.filter(user=user).order_by("-order_date")

        for order in last_orders:
            total_value = 0
            purchased_courses = order.purchased_courses.all()
            for purchased_course in purchased_courses:
                total_value += purchased_course.course.price * purchased_course.quantity

            order.total_value = total_value

        if last_orders:
            paginator = Paginator(last_orders, self.default_pagination_size)
            page_number = request.GET.get("page")
            paginated_last_orders = paginator.get_page(page_number)

        context = {
            "user": user,
            "isMember": isMember,
            "orders": paginated_last_orders,
        }
        return render(request, self.template_name, context)


