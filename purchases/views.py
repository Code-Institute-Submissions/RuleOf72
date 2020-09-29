from django.shortcuts import render, get_object_or_404, HttpResponse, reverse
from django.conf import settings
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
import stripe
from lessons.models import Lesson
from .models import Purchase

def checkout(request, lesson_id):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    current_site = Site.objects.get_current()
    domain = current_site.domain
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    line_items = [{
            "name": lesson.topic,
            # multiply the actual cost of the book to represent
            # the cost in cents and must be in integer
            "amount": lesson.price,
            "quantity": 1,
            "currency": "usd"
        }]
    session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                client_reference_id=request.user.id,
                mode='payment',
                line_items=line_items,
                success_url=domain + reverse('checkout_success_route'),
                cancel_url=domain + reverse('checkout_cancelled_route'),
                metadata={
                    "data": json.dumps({
                        'lesson_id': lesson.id
                    })
                }
            )
    return render(request, 'purchases/checkout.template.html', {
        'session_id': session.id,
        'public_key': stripe_publishable_key,
    })

def checkout_success(request):
    return HttpResponse("Payment is successful")


def checkout_cancelled(request):
    return HttpResponse("Payment cancelled")

@csrf_exempt
def payment_completed(request):
    # payload represents the data sent back to us by Stripe
    payload = request.body
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # invalid payload
        print(e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print(e)
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        handle_payment(session)

    return HttpResponse(status=200)

def handle_payment(session):
    user = get_object_or_404(User, pk=session["client_reference_id"])
    metadata = json.loads(session['metadata']['data'])
    lesson = get_object_or_404(Lesson, pk=metadata['lesson_id'])

    purchase = Purchase()
    purchase.lesson_purchased = lesson
    purchase.student = user
    purchase.price = lesson.price
    purchase.save()


# from django.shortcuts import render, get_object_or_404, HttpResponse, reverse
# from django.conf import settings
# from django.contrib.sites.models import Site
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.models import User
# import stripe
# import json

# # Create your views here.


# def checkout(request):

#     # setup stripe
#     stripe.api_key = settings.STRIPE_SECRET_KEY

#     # retrive the shopping cart
#     # store all the line items in this list
#     line_items = []

#     # for each item in the shopping cart...
#     item = {
#         "name": 'aa',
#         # multiply the actual cost of the book to represent
#         # the cost in cents and must be in integer
#         "amount": 1000,
#         "quantity": 1,
#         "currency": "usd"
#     }

#     line_items.append(item)
#     # get the domain name
#     current_site = Site.objects.get_current()
#     domain = current_site.domain

#     # pass all the line items to stripe and in return
#     # get a checkout session id
#     session = stripe.checkout.Session.create(
#         payment_method_types=['card'],
#         line_items=line_items,
#         client_reference_id=request.user.id,
#         mode='payment',
#         success_url=domain + reverse('checkout_success_route'),
#         cancel_url=domain + reverse('checkout_cancelled_route'),
#         metadata={
#             "books": json.dumps([1])
#         }
#     )

#     # render the template which will redirect to stripe
#     return render(request, 'purchases/checkout.template.html', {
#         'session_id': session.id,
#         'public_key': settings.STRIPE_PUBLISHABLE_KEY
#     })


# def checkout_success(request):
#     # empty the shopping cart
#     # request.session['shopping_cart'] = {}
#     return HttpResponse("Payment is successful")


# def checkout_cancelled(request):
#     return HttpResponse("Payment cancelled")


# @csrf_exempt
# def payment_completed(request):
#     # payload represents the data sent back to us by Stripe
#     payload = request.body
#     endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
#     sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
#     event = None

#     try:
#         event = stripe.Webhook.construct_event(
#             payload, sig_header, endpoint_secret
#         )
#     except ValueError as e:
#         # invalid payload
#         print(e)
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError as e:
#         print(e)
#         return HttpResponse(status=400)

#     if event['type'] == 'checkout.session.completed':
#         session = event['data']['object']
#         # handle_payment(session)

#     return HttpResponse(status=200)


# def handle_payment(session):
#     user = get_object_or_404(User, pk=session["client_reference_id"])

#     all_book_ids = json.loads(session['metadata']['books'])
#     for book in all_book_ids:
#         book_model = get_object_or_404(Book, pk=book["book_id"])

#         # create a Purchase model manually
#         purchase = Purchase()
#         purchase.book = book_model
#         purchase.user = user
#         purchase.price = book_model.cost
#         purchase.qty = int(book["qty"])
#         purchase.save()