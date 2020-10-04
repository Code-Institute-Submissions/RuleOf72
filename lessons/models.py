from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Lesson(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    topic = models.CharField(blank=False, max_length=255)
    price = models.PositiveIntegerField(blank=False, default=0)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    introduction = models.TextField(blank=True)
    picture = CloudinaryField()

    def __str__(self):
        return str(self.topic) + ' by: ' + str(self.teacher.username)

class Sub_topic(models.Model):
    title = models.CharField(blank=False, max_length=255)
    video = models.CharField(blank=True, max_length=255)
    content = models.TextField(blank=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

