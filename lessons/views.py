from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from .forms import Lessons_form, Subtopics_form
from .models import Lesson, Sub_topic
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

# Create your views here.
def all_lessons(request):
    all_lessons = Lesson.objects.all()
    return render(request, "all_lessons.template.html", {
        'all_lessons': all_lessons
    })

@login_required
def create_lesson(request):
    if request.method == "POST":
        form = Lessons_form(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.teacher = request.user
            lesson.save()
            messages.success(request, f"New lesson {form.cleaned_data['topic']} has been created")
            return redirect(reverse(all_lessons))
        else:
            return render(request, 'create_lessons.template.html', {
                'form': form
            })
    else:
        form = Lessons_form()
        return render(request, 'create_lessons.template.html', {
            'form': form
        })

@login_required
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

@login_required    
def delete_lesson(request, lesson_id):
    lesson_being_deleted = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == "POST":
        lesson_being_deleted.delete()
        return redirect(reverse(all_lessons))
    else:
        return render(request, 'delete_lessons.template.html', {
            "lesson": lesson_being_deleted
        })

def specific_lesson(request, lesson_id):
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'specific_lessons.template.html', {
        'lesson': lesson_being_viewed
    })

@login_required
def add_sub_topic(request, lesson_id):
    form = Subtopics_form(request.POST)
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == "POST":
        if form.is_valid():
            subtopic = form.save(commit=False)
            subtopic.lesson = get_object_or_404(Lesson, pk=lesson_id)
            subtopic.save()
            return redirect(reverse('specific_lesson_route',
                                    kwargs={
                                        'lesson_id': lesson_id
                                    }))
        else:
            return render(request, 'add_sub_topic.template.html', {
                'form': form,
                'lesson': lesson_being_viewed
            })
    else:
        form = Subtopics_form()
        return render(request, 'add_sub_topic.template.html', {
            'form': form,
            'lesson': lesson_being_viewed
        })

@login_required
def update_sub_topic(request, lesson_id, sub_topic_id):
    # 1. retrieve the book that we are editing
    topic_being_updated = get_object_or_404(Sub_topic, pk=sub_topic_id)
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    # 2. if the update form is submitted
    sub_topic_form = Subtopics_form(request.POST, instance=topic_being_updated)
    if request.method == "POST":
        if sub_topic_form.is_valid():
            sub_topic_form.save()
            return redirect(reverse(all_lessons))
        else:
            return render(request, 'update_sub_topic.template.html', {
                "form": sub_topic_form,
                "lesson": lesson_being_viewed,
                "sub_topic": topic_being_updated
            })
    else:
        # 4. create a form with the book details filled in
        sub_topic_form = Subtopics_form(instance=topic_being_updated)
        return render(request, 'update_sub_topic.template.html', {
            "form": sub_topic_form,
            'sub_topic': topic_being_updated,
            "lesson": lesson_being_viewed
        })

@login_required
def delete_sub_topic(request, lesson_id, sub_topic_id):
    topic_being_deleted = get_object_or_404(Sub_topic, pk=sub_topic_id)
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == "POST":
        topic_being_deleted.delete()
        return redirect(reverse('specific_lesson_route',
                                    kwargs={
                                        'lesson_id': lesson_id,
                                        'sub_topic_id': sub_topic_id
                                    }))
    else:
        return render(request, 'delete_sub_topic.template.html', {
            "sub_topic": topic_being_deleted,
            "lesson": lesson_being_viewed
        })