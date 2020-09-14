from django.urls import path
import lessons.views


urlpatterns = [
    path('create/', lessons.views.create_lesson),
    path('update/<lesson_id>/', lessons.views.update_lesson, name='update_lesson_route'),
    path('lessons/', lessons.views.all_lessons),
]