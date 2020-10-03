from django.shortcuts import render, get_object_or_404, HttpResponse, reverse, redirect
from django.conf import settings
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
import stripe
from . import views
from lessons.models import Lesson
from .models import Purchase
from django.contrib.auth.decorators import login_required


@login_required
def checkout(request, lesson_id):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    current_site = Site.objects.get_current()
    domain = current_site.domain
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    line_items = [{
            "name": lesson.topic,
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
    lesson = Purchase.objects.filter(student=request.user)
    return render(request, "lessons/purchased_lessons.template.html", {
        'lessons': lesson
    })


def checkout_cancelled(request):
    return redirect(reverse("all_lesson_route"))


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
