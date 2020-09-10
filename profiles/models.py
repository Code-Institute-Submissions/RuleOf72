from django.db import models
from django.contrib.auth.models import User
from lessons.models import Lesson, Sub_topic
from purchases.models import Purchase
# Create your models here.

class Profile(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    topic = models.ForeignKey(Sub_topic, on_delete=models.CASCADE)
    purchases = models.ForeignKey(Purchase, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.username + "'s Profile"