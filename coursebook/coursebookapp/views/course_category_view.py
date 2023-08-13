from django.shortcuts import render
from rest_framework import generics

from ..models.course import Course

# from ..models.instructor import Instructor
# from ..models.course_image import CourseImage
from ..serializers import CourseSerializer


class CourseCategoryView(generics.ListAPIView):
    serializer_class = CourseSerializer
    template_name = "pages/course-category.html"

    def get(self, request, *args, **kwargs):
        province_slug = self.kwargs.get("province_slug")

        if province_slug:
            courses = Course.objects.filter(province_slug=province_slug)
            for course in courses:
                image = course.courseimage_set.first()
                course.image = image
        else:
            courses = {}

        context = {
            "courses": courses,
        }
        return render(request, self.template_name, context)
