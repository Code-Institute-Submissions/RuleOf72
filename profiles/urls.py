from django.urls import path
import profiles.views


urlpatterns = [
    path('', profiles.views.show_profile),
]
