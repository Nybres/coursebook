from rest_framework import generics

from django.shortcuts import render
from rest_framework import generics

from ..serializers import CartSerializer


class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    template_name = "pages/cart.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
