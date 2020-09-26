from django.urls import path
import forum.views


urlpatterns = [
    path('<lesson_id>/', forum.views.show_forum, name="show_forum_route"),
    path('create/<lesson_id>/', forum.views.create_forum, name="create_forum_route"),
    path('update/<lesson_id>/<topic_id>/', forum.views.update_forum, name="update_forum_route"),
    path('delete/<lesson_id>/<topic_id>/', forum.views.delete_forum, name="delete_forum_route"),
    path('<lesson_id>/<topic_id>/', forum.views.show_specific_topic, name="specific_topic_route"),
    path('<lesson_id>/<topic_id>/create/comment/', forum.views.create_comment, name="create_comment_route"),
    path('<lesson_id>/<topic_id>/<comment_id>/update/', forum.views.update_comment, name="update_comment_route"),

]

