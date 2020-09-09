from django.shortcuts import render, HttpResponse, get_object_or_404

from .forms import lessonsForm
from .models import lessons

# Create your views here.

def create_lesson(request):
    if request.method == "POST":
        form = lessonsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Lesson is added")
        else:
            return render(request, 'lessons/create_lessons.template.html', {
                'form': form
            })
    else:
        form = lessonsForm()

        return render(request, 'lessons/create_lessons.template.html', {
            'form': form
        })