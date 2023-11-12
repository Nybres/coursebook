from django.shortcuts import render
from django.urls import reverse
from django.urls import resolve
from django.core.paginator import Paginator
from rest_framework import generics

from ..models.blog_post import BlogPost
from ..models.blog_category import BlogCategory
from ..serializers import BlogPostSerializer


class BlogCategoryView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    template_name = "pages/blog.html"
    default_page_size = 1

    def get(self, request, *args, **kwargs):
        # province_slug = self.kwargs.get("province_slug")

        # if province_slug:
        #     courses = Course.objects.filter(province_slug=province_slug)
        #     for course in courses:
        #         image = course.courseimage_set.first()
        #         course.image = image
        # else:
        #     courses = {}
        posts = BlogPost.objects.all()
        categories = BlogCategory.objects.all()

        paginator = Paginator(posts, self.default_page_size)
        page_number = request.GET.get("page")
        paginated_posts = paginator.get_page(page_number)
        breadcrumbs = [
            ("Coursebook", reverse("home")),
            ("Blog", reverse("blog")),
        ]

        context = {
            "posts": paginated_posts,
            'categories': categories,
            "breadcrumbs": breadcrumbs,
        }
        return render(request, self.template_name, context)
