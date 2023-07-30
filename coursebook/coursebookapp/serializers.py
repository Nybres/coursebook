from rest_framework import serializers
from django.contrib.auth.models import Group


from .models.app_user import AppUser
from .models.instructor import Instructor
from .models.course import Course
from .models.course_image import CourseImage


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = [
            "id",
            "company_name",
            "password",
            "email",
            "phone_number",
            "first_name",
            "last_name",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        group = self.get_group_name_from_url()
        user = AppUser.objects.create_user(
            username=validated_data.get("email", ""), **validated_data
        )
        user.groups.add(group)
        return user

    def get_group_name_from_url(self):
        url = self.context.get("request").path
        group_name = "customer" if "register-customer" in url else "company"

        return Group.objects.get(name=group_name)


class InstructorSerializer(serializers.ModelSerializer):
    app_user = serializers.CharField(required=False)
    photo = serializers.ImageField(required=False)

    class Meta:
        model = Instructor
        fields = "__all__"

    def create(self, validated_data):
        app_user_id = self.context.get("request").user.id
        app_user = AppUser.objects.get(id=app_user_id)
        instructor = Instructor.objects.create(app_user=app_user, **validated_data)
        return instructor


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseImage
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=True, use_url=False),
        write_only=True,
        required=False,
    )

    class Meta:
        model = Course
        fields = "__all__"

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])
        course = Course.objects.create(**validated_data)
        images_to_save = []
        for image in uploaded_images:
            images_to_save.append(CourseImage(course=course, image=image))
        CourseImage.objects.bulk_create(images_to_save)
        return course
