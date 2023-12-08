from django.shortcuts import render
from rest_framework import generics


class GalleryView(generics.ListCreateAPIView):
    template_name = "pages/gallery.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
