from django.shortcuts import render

from rest_framework import generics

from ..serializers import AppUserSerializer


class RegisterView(generics.ListCreateAPIView):
    serializer_class = AppUserSerializer

    def get(self, request, *args, **kwargs):
        template_name = self.get_template_name_from_url(request)
        return render(request, template_name)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
        return render(request, self.template_name, {"serializer": serializer})

    def get_template_name_from_url(self, request):
        url = request.path
        template_name = (
            "register-customer.html"
            if "register-customer" in url
            else "register-company.html"
        )
        return "pages/" + template_name
