from rest_framework import generics
from ..models import Course, Cart
from ..serializers import CartItemSerializer
from rest_framework.response import Response
from rest_framework import status


class AddToCartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            self.perform_create(serializer)
            response_data = {"message": "Produkt został dodany do koszyka."}
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {
                "error": "Nie udało się dodać produktu do koszyka.",
                "details": serializer.errors,
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)