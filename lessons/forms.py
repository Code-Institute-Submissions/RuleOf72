from django import forms
from .models import lessons, User

class lessonsForm(forms.ModelForm):
    class Meta:
        model = lessons
        fields = "__all__"