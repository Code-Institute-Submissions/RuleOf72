from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from .forms import Lessons_form, Subtopics_form
from .models import Lesson, Sub_topic

# Create your views here.
def all_lessons(request):
    all_lessons = Lesson.objects.all()
    return render(request, "all_lessons.template.html", {
        'all_lessons': all_lessons
    })

def create_lesson(request):
    if request.method == "POST":
        form = Lessons_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Lesson is added")
        else:
            return render(request, 'create_lessons.template.html', {
                'form': form
            })
    else:
        form = Lessons_form()
        return render(request, 'create_lessons.template.html', {
            'form': form
        })


def update_lesson(request, lesson_id):
    # 1. retrieve the book that we are editing
    lesson_being_updated = get_object_or_404(Lesson, pk=lesson_id)

    # 2. if the update form is submitted
    if request.method == "POST":

        # 3. create the form and fill in the user's data. Also specify that
        # this is to update an existing model (the instance argument)
        lesson_form = Lessons_form(request.POST, instance=lesson_being_updated)
        if lesson_form.is_valid():
            lesson_form.save()
            return redirect(reverse(all_lessons))
        else:
            return render(request, 'update_lessons.template.html', {
                "form": lesson_form
            })
    else:
        # 4. create a form with the book details filled in
        lesson_form = Lessons_form(instance=lesson_being_updated)
        return render(request, 'update_lessons.template.html', {
            "form": lesson_form
        })