from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..helpers import check_membership
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from ..serializers import OrderHistorySerializer

from ..models import OrderHistory
from ..models import Participant
from ..models import PurchasedCourse


@method_decorator(login_required(login_url="login"), name="dispatch")
class AccountView(generics.ListAPIView):
    template_name = "pages/account.html"
    # serializer_class = OrderHistorySerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        isMember = check_membership(user)

        last_5_orders = OrderHistory.objects.order_by("-order_date")[:5]
        orders_with_details = []
        for order in last_5_orders:
            order_details = {
                "order_id": order.id,
                "order_date": order.order_date,
                "purchased_courses": [],
            }
            purchased_courses = order.purchased_courses.all()

            for purchased_course in purchased_courses:
                course = purchased_course.course

                first_image = course.courseimage_set.first()
                image_url = first_image.image_thumb.url if first_image else None

                participants = Participant.objects.filter(
                    purchased_course=purchased_course
                )

                order_details["purchased_courses"].append(
                    {
                        "course_title": course.title,
                        "course_image_url": image_url,
                        "participants": list(
                            participants.values("name", "surname", "email", "phone")
                        ),
                    }
                )

            orders_with_details.append(order_details)

        sold_orders = get_last_8_purchased_courses_with_details(user)

        # serializer = self.serializer_class(orders, many=True)
        # serialized_data = serializer.data
        context = {
            "user": user,
            "isMember": isMember,
            "orders": orders_with_details,
            "sold_orders": sold_orders,
            # "orders": JSONRenderer().render(serialized_data).decode('utf-8'),
        }
        return render(request, self.template_name, context)


def get_last_8_purchased_courses_with_details(user):
    user_purchased_courses = PurchasedCourse.objects.filter(
        course__instructor__app_user=user
    ).order_by("-id")[:8]

    courses_with_details = []
    for purchased_course in user_purchased_courses:
        course = purchased_course.course
        instructor = course.instructor

        first_image = course.courseimage_set.first()
        image_url = first_image.image_thumb.url if first_image else None

        courses_with_details.append(
            {
                "course_title": course.title,
                "course_description": course.course_description,
                "instructor_name": instructor.fullname,
                "course_image": image_url,
                "course_price": course.price,
                "quantity": purchased_course.quantity,
                # Dodaj inne informacje o kursie, które chcesz wyświetlić
            }
        )

    return courses_with_details
