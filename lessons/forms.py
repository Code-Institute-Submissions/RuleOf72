from django import forms
from .models import Lessons, Subtopics
from django.contrib.auth.models import User

class LessonsForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = "__all__"

class SubtopicsForm(forms.ModelForm):
    class Meta:
        model = Subtopics
        fields = "__all__"