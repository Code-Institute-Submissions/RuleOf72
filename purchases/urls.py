from django.urls import path
import purchases.views

urlpatterns = [
    path('success/', purchases.views.checkout_success,
         name='checkout_success_route' ),
    path('cancelled/', purchases.views.checkout_cancelled,
         name="checkout_cancelled_route"),
    path('payment_completed/', purchases.views.payment_completed,
         name="payment_completed_route"),
    path('lesson/<lesson_id>/', purchases.views.checkout, name="checkout_route"),
]