from django.shortcuts import render
from rest_framework import generics

class AboutUsView(generics.ListCreateAPIView):
    template_name = "pages/about_us.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
