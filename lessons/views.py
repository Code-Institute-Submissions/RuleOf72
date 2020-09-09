from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import LessonsForm, SubtopicsForm
from .models import Lesson, Sub_topic

# Create your views here.

def create_lesson(request):
    if request.method == "POST":
        form = LessonsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Lesson is added")
        else:
            return render(request, 'create_lessons.template.html', {
                'form': form
            })
    else:
        form = LessonsForm()

        return render(request, 'create_lessons.template.html', {
            'form': form
        })