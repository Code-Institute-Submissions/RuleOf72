from django import forms
from .models import Lesson, Sub_topic
from django.contrib.auth.models import User

class LessonsForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = "__all__"

class SubtopicsForm(forms.ModelForm):
    class Meta:
        model = Sub_topic
        fields = "__all__"