from django.contrib import admin
from .models.app_user import AppUser
from .models.instructor import Instructor
from .models.course import Course

from .models.course_image import CourseImage
from .models.cart import Cart
from .models.cart_item import CartItem
# from .models.purchased_course import PurchasedCourse
from .models.blog_category import BlogCategory
from .models.blog_post import BlogPost


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "instructor", "price", "seats", "date")


class AppUserAdmin(admin.ModelAdmin):
    list_display = ("email", "company_name", "first_name", "last_name")


class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "course", "quantity")


admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Instructor)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseImage)
admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)
# admin.site.register(PurchasedCourse)
admin.site.register(BlogCategory)
admin.site.register(BlogPost)
