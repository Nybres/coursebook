from django.shortcuts import render
from rest_framework import generics

from ..models.course import Course


class HomeView(generics.ListCreateAPIView):
    template_name = "pages/index.html"

    def get(self, request, *args, **kwargs):
        # recommended_courses = Course.objects.filter(instructor__isnull=False)
        recommended_courses = Course.objects.all()

        for course in recommended_courses:
            # images = CourseImage.objects.filter(course=course)
            image = course.courseimage_set.first()
            course.image = image

        context = {
            "recommended_courses": recommended_courses,
        }
        return render(request, self.template_name, context)
