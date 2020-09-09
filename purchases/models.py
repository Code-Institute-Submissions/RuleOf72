from django.db import models
from lessons.models import Lessons
from django.contrib.auth.models import User
# Create your models here.

class Purchase(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_purchased = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.student.username + ' purchased ' + self.lesson_purchased.topic + ' on ' + date_purchased