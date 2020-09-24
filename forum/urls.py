from django.urls import path
import forum.views


urlpatterns = [
    path('<lesson_id>/', forum.views.show_forum, name="show_forum_route"),
    path('create/<lesson_id>/', forum.views.create_forum, name="create_forum_route"),
]

