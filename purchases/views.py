from django.shortcuts import render, get_object_or_404, HttpResponse, reverse
from django.conf import settings
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

import stripe
from lessons.models import Lesson

# Create your views here.

def checkout(request, lesson_id):
    if request.method == 'GET':
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
        return render(request, 'purchase.template.html', {
                'publishable_key':stripe_publishable_key,
                'price_in_dollars':lesson.price,
                'price':int(lesson.price)*100,
                'lesson': lesson
            })
    else:
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe_token = request.POST["stripeToken"]
        charge = stripe.Charge.create(price=request.POST["lesson.price"],
            currency='usd',
            source=stripe_token
        )
        return HttpResponse("Thank you for your donation")

def checkout_success(request):
    return HttpResponse("Payment is successful")


def checkout_cancelled(request):
    return HttpResponse("Payment cancelled")

# @csrf_exempt
# def payment_completed(request):
#     payload = request.body
#     sig_header = request.META['HTTP_STRIPE_SIGNATURE']
#     event = None

#     try:
#         event = stripe.Webhook.construct_event(
#         payload, sig_header, endpoint_secret
#         )
#     except ValueError as e:
#         # Invalid payload
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError as e:
#         # Invalid signature
#         return HttpResponse(status=400)

#     # Handle the checkout.session.completed event
#     if event['type'] == 'checkout.session.completed':
#         session = event['data']['object']

#         # Fulfill the purchase...
#         handle_payment(session)

#     return HttpResponse(status=200)