from django.shortcuts import render
from rest_framework import generics

class FaqView(generics.ListCreateAPIView):
    template_name = "pages/faq.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
