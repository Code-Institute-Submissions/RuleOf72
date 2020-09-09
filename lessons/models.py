from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class lessons(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    topic = models.CharField(blank=False, max_length=255)
    price = models.FloatField(blank=False, default=0)

