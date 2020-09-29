from django.urls import path
import lessons.views


urlpatterns = [
    path('create/', lessons.views.create_lesson, name='create_lesson_route'),
    path('update/<lesson_id>/', lessons.views.update_lesson, name='update_lesson_route'),
    path('lessons/', lessons.views.all_lessons, name='all_lesson_route'),
    path('delete/<lesson_id>/', lessons.views.delete_lesson, name='delete_lesson_route'),
    path('lessons/<lesson_id>/', lessons.views.specific_lesson, name='specific_lesson_route'),
    path('lessons/<lesson_id>/addtopic/', lessons.views.add_sub_topic, name='add_sub_topic_route'),
    path('lessons/<lesson_id>/updatetopic/<sub_topic_id>/', lessons.views.update_sub_topic, name='update_sub_topic_route'),
    path('delete/<lesson_id>/topic/<sub_topic_id>/', lessons.views.delete_sub_topic, name='delete_sub_topic_route'),
    path('created/', lessons.views.created_lessons, name='created_lesson_route'),
    path('purchased/', lessons.views.purchased_lessons, name='purchased_lesson_route'),
]