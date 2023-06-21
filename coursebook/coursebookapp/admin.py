from django.contrib import admin
from .models.app_user import AppUser
from .models.instructor import Instructor
from .models.course import Course

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Instructor)
admin.site.register(Course)
