from django.shortcuts import render
from django.urls import reverse
from django.urls import resolve
from django.shortcuts import render, get_object_or_404
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
        category_id = self.kwargs.get("category_id")
        categories = BlogCategory.objects.all()
        
        
        
        if category_id:
            category = get_object_or_404(BlogCategory, id=category_id)
            posts = BlogPost.objects.filter(categories=category)
            breadcrumbs = [
            ("Coursebook", reverse("home")),
            ("Blog", reverse("blog")),
            (category.name, reverse("blog_category", kwargs={"category_id": category_id})),
            ]
        else:
            posts = BlogPost.objects.all()     
            breadcrumbs = [
            ("Coursebook", reverse("home")),
            ("Blog", reverse("blog")),
            ] 


        paginator = Paginator(posts, self.default_page_size)
        page_number = request.GET.get("page")
        paginated_posts = paginator.get_page(page_number)


        context = {
            "posts": paginated_posts,
            'categories': categories,
            "breadcrumbs": breadcrumbs,
        }
        return render(request, self.template_name, context)
