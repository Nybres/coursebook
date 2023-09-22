from rest_framework.generics import RetrieveUpdateAPIView
from ..models import Course
from ..models.course_image import CourseImage
from ..serializers import CourseSerializer
from ..serializers import ImageSerializer
from django.http import JsonResponse


class EditCourseView(RetrieveUpdateAPIView):
    serializer_class = CourseSerializer

    queryset = Course.objects.all()

    def get(self, request, *args, **kwargs):
        course_pk = kwargs.get('pk', None)
        course = Course.objects.get(pk=course_pk)

        course_images = CourseImage.objects.filter(course=course)
        images_data = []

        for image in course_images:
            image_serializer = ImageSerializer(image, context={'request': request})
            images_data.append(image_serializer.data)

        serializer = self.serializer_class(course)
        serialized_data = serializer.data

        serialized_data['images'] = images_data

        return JsonResponse(serialized_data, status=200)
