from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def create_checkout_session(request):
    cart_items = [
        {
            "price_data": {
                "currency": "pln",
                "product_data": {
                    "name": "Kurs gotowania test z palca",
                },
                "unit_amount": 19900,
            },
            "quantity": 2,
        },
        {
            "price_data": {
                "currency": "pln",
                "product_data": {
                    "name": "Kurs gotowania test z palca 2",
                },
                "unit_amount": 8900,
            },
            "quantity": 1,
        },
    ]

    session = stripe.checkout.Session.create(
        success_url="http://localhost:8000/",
        cancel_url="http://localhost:8000/login",
        payment_method_types=["card"],
        line_items=cart_items,
        mode="payment",
        submit_type="auto",
    )

    return JsonResponse({"id": session.id})
