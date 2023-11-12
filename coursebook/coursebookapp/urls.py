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
        "account-blog",
        views.AccountBlogView.as_view(),
        name="account_blog",
    ),
    path(
        "blog/post/<int:pk>",
        views.PostDetailView.as_view(),
        name="post",
    ),
     path(
        "blog",
        views.BlogCategoryView.as_view(),
        name="blog",
    ),
      path(
        "blog/category/<int:category_id>/",
        views.BlogCategoryView.as_view(),
        name="blog_category",
    ),
    path(
        "account-blog/<int:pk>",
        views.BlogPostModify.as_view(),
        name="account_blog_modify",
    ),
    path(
        "course/<str:province_slug>/<str:slug>/",
        views.CourseDetailView.as_view(),
        name="course_detail",
    ),
    path(
        "courses/<str:province_slug>",
        views.CourseCategoryView.as_view(),
        name="course_category",
    ),
    path(
        "edit-instructor/<int:pk>",
        views.EditInstructorView.as_view(),
        name="edit_instructor",
    ),
    path(
        "edit-course/<int:pk>",
        views.EditCourseView.as_view(),
        name="edit_course",
    ),
    path(
        "cart",
        views.CartView.as_view(),
        name="cart",
    ),
    path(
        "mini-cart",
        views.MiniCartView.as_view(),
        name="mini_cart",
    ),
    path(
        "cart/add",
        views.AddToCartView.as_view(),
        name="add_to_cart",
    ),
    path(
        "cart/increase-quantity/<int:pk>",
        views.IncreaseCartItemQuantityView.as_view(),
        name="increase-cart-item-quantity",
    ),
    path(
        "cart/remove/<int:pk>/",
        views.RemoveFromCartView.as_view(),
        name="remove_from_cart",
    ),
    path(
        "create-checkout-session",
        views.create_checkout_session,
        name="create_checkout_session",
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
