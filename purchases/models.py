from django.db import models
from lessons.models import Lesson
from django.contrib.auth.models import User


class Purchase(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_purchased = models.ForeignKey(Lesson, on_delete=models.CASCADE,
                                         related_name='purchased')
    date_purchased = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return (self.student.username + ' purchased ' +
                self.lesson_purchased.topic)
