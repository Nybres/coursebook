from django.shortcuts import render
from django.urls import reverse
from django.urls import resolve
from django.core.paginator import Paginator
from rest_framework import generics

from ..models.course import Course
from ..serializers import CourseSerializer


class CourseCategoryView(generics.ListAPIView):
    serializer_class = CourseSerializer
    template_name = "pages/course-category.html"
    default_page_size = 9

    def get(self, request, *args, **kwargs):
        province_slug = self.kwargs.get("province_slug")

        if province_slug:
            courses = Course.objects.filter(province_slug=province_slug, available=True)
            for course in courses:
                image = course.courseimage_set.first()
                course.image = image
        else:
            courses = {}

        paginator = Paginator(courses, self.default_page_size)
        page_number = request.GET.get("page")
        paginated_courses = paginator.get_page(page_number)
        breadcrumbs = [
            ("Coursebook", reverse("home")),
            (
                province_slug,
                reverse("course_category", kwargs={"province_slug": province_slug}),
            ),
        ]

        context = {
            "courses": paginated_courses,
            "breadcrumbs": breadcrumbs,
        }
        return render(request, self.template_name, context)
