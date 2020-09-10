from django.urls import path
import forum.views


urlpatterns = [
    path('', forum.views.show_forum),
]

