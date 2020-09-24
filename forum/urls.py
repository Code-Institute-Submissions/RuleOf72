from django.urls import path
import forum.views


urlpatterns = [
    path('', forum.views.show_forum),
    path('create/', forum.views.create_forum, name="create_forum_route"),
]

