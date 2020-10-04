from django.urls import path
import checkout.views

urlpatterns = [
    path('success/', checkout.views.checkout_success,
         name='checkout_success_route'),
    path('cancelled/', checkout.views.checkout_cancelled,
         name="checkout_cancelled_route"),
    path('payment_completed/', checkout.views.payment_completed,
         name="payment_completed_route"),
    path('lesson/<lesson_id>/', checkout.views.checkout,
         name="checkout_route"),
]
