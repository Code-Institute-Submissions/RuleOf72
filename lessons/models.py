from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Lessons(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    topic = models.CharField(blank=False, max_length=255)
    price = models.IntegerField(blank=False, default=0)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic + ' by: ' + self.teacher.username

class Subtopics(models.Model):
    title = models.CharField(blank=False, max_length=255)
    vid = models.CharField(blank=True, max_length=255)
    content = models.TextField(blank=False)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

