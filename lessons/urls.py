from django.urls import path
import lessons.views


urlpatterns = [
    path('create/', lessons.views.create_lesson)
]