from rest_framework import serializers

from django.contrib.auth.models import Group



from .models.app_user import AppUser
from .models.instructor import Instructor


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
    class Meta:
        model = Instructor
        fields = '__all__'

    def create(self, validated_data):
        app_user_id = self.context.get("request").user.id
        app_user = AppUser.objects.get(id=app_user_id)
        instructor = Instructor.objects.create(app_user=app_user, **validated_data)
        return instructor