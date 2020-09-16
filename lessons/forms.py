from django import forms
from .models import Lesson, Sub_topic
from django.contrib.auth.models import User

class Lessons_form(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = "__all__"

class Subtopics_form(forms.ModelForm):
    class Meta:
        model = Sub_topic
        fields = ('title', 'vid', 'content')