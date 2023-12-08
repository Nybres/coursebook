from django.shortcuts import render
from rest_framework import generics

class ContactView(generics.ListCreateAPIView):
    template_name = "pages/contact.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
