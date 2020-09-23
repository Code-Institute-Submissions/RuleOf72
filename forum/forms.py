from django import forms
from lessons.models import Lesson, Sub_topic
from .models import Forum_comment, Forum_topic 
from django.contrib.auth.models import User

class Forum_form(forms.ModelForm):
    class Meta:
        model = Forum_topic
        fields = ('title', 'content')

class Comment_form(forms.ModelForm):
    class Meta:
        model = Forum_comment
        fields = ('title', 'content')