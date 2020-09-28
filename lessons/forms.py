from django import forms
from .models import Lesson, Sub_topic
from django.contrib.auth.models import User

class Lessons_form(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('topic', 'introduction', 'picture', 'price')

class Subtopics_form(forms.ModelForm):
    class Meta:
        model = Sub_topic
        fields = ('title', 'vid', 'content')

class SearchForm(forms.Form):
    topic = forms.CharField(max_length=255, required=False)