from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("login", views.UserLoginView.as_view(), name="login"),
    path("logout", views.UserLogoutView.as_view(), name="logout"),
    path("register-customer", views.RegisterView.as_view(), name="register_customer"),
    path("register-company", views.RegisterView.as_view(), name="register_company"),
    # account
    path("account", views.AccountView, name="account"),
    path("account-courses", views.AccountCoursesView.as_view(), name="account_courses"),
    path(
        "delete-course/<int:pk>/",
        views.AccountCourseDelete.as_view(),
        name="delete_course",
    ),
    path(
        "delete-instructor/<int:pk>/",
        views.AccountInstructorDelete.as_view(),
        name="delete_instructor",
    ),
    path(
        "account-instructors",
        views.AccountInstructorsView.as_view(),
        name="account_instructors",
    ),
    path(
        "course/<str:province_slug>/<str:slug>/",
        views.CourseDetailView.as_view(),
        name="course_detail",
    ),
     path(
        "course/<str:province_slug>",
        views.CourseCategoryView.as_view(),
        name="course_category",
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
