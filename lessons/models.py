from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Lesson(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    topic = models.CharField(blank=False, max_length=255)
    price = models.IntegerField(blank=False, default=0)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="gallery")
    introduction = models.TextField(blank=True)

    def __str__(self):
        return self.topic + ' by: ' + self.teacher.username

class Sub_topic(models.Model):
    title = models.CharField(blank=False, max_length=255)
    vid = models.CharField(blank=True, max_length=255)
    content = models.TextField(blank=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

