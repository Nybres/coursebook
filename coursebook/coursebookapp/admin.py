from django.contrib import admin
from .models.app_user import AppUser
from .models.instructor import Instructor
from .models.course import Course

from .models.course_image import CourseImage


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "instructor", "price", "seats", "date")


class AppUserAdmin(admin.ModelAdmin):
    list_display = ("email", "company_name", "first_name", "last_name")


admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Instructor)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseImage)
