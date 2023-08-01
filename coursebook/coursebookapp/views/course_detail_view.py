from django.shortcuts import render
from rest_framework import generics

from ..models.course import Course
from ..models.instructor import Instructor
from ..models.course_image import CourseImage
from ..serializers import CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = "slug"
    template_name = "pages/course_detail.html"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        random_courses = Course.objects.order_by("?")[:6]
        # user = request.user
        # instructor = Instructor.objects.filter(instructor=instance.instructor)

        # image = instance.courseimage_set.first()
        # if image:
        #     instance.image = image

        context = {
            "course": instance,
            "random_courses": random_courses,
        }

        return render(request, self.template_name, context)
