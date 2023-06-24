from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import generics

from ..models.course import Course
from ..models.instructor import Instructor
from ..serializers import CourseSerializer
from ..helpers import check_membership

@method_decorator(login_required(login_url='login'), name='dispatch')
class AccountCoursesView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    template_name = 'pages/account-courses.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        isMember = check_membership(user)
        instructors = Instructor.objects.filter(app_user=user)
        provinces = Course.province_choices


        courses = Course.objects.filter(instructor__app_user=user)
        context = {
                'user':user,
                'isMember':isMember,
                "courses":courses,
                "provinces":provinces,
                "instructors":instructors,
            }
        
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
        else:
            print(serializer.errors)
        return redirect('account_courses')
