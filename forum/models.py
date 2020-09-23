from django.db import models
from lessons.models import Lesson
from django.contrib.auth.models import User
# Create your models here.

class Forum_topic(models.Model):
    title = models.CharField(blank=False, max_length=255)
    content = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_commented = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.commenter.username + "'s thread"

class Forum_comment(models.Model):
    title = models.CharField(blank=False, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    commenter = commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_commented = models.ForeignKey(Forum_topic, on_delete=models.CASCADE)
    content = models.TextField(blank=False)

    def __str__(self):
        return 'Commented by: ' + self.commenter.username
