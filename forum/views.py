from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from lessons.forms import Lessons_form, Subtopics_form
from lessons.models import Lesson, Sub_topic
from .forms import Forum_form, Comment_form
from .models import Forum_comment, Forum_topic
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
# Create your views here.

@login_required
def show_forum(request, lesson_id):
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'forum_topic.template.html', {
        'lesson': lesson_being_viewed, 
        'discussions': Forum_topic.objects.filter(lesson_commented_id=lesson_id)
        })

@login_required
def create_forum(request, lesson_id):
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == "POST":
        form = Forum_form(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.commenter = request.user
            forum.lesson_commented = lesson_being_viewed
            forum.save()
            messages.success(request, f"New Forum Topic {form.cleaned_data['title']} has been created")
            return redirect(reverse('show_forum_route', kwargs={
                                        'lesson_id': lesson_id
                                    }))
        else:
            return render(request, 'create_forum.template.html', {
                'form': form,
                'lesson': lesson_being_viewed
            })
    else:
        form = Forum_form()
        return render(request, 'create_forum.template.html', {
            'form': form,
            'lesson': lesson_being_viewed
        })

@login_required
def update_forum(request, lesson_id, topic_id):
    # 1. retrieve the book that we are editing
    forum_being_viewed = get_object_or_404(Forum_topic, pk=topic_id)
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    # 2. if the update form is submitted
    if request.method == "POST":

        # 3. create the form and fill in the user's data. Also specify that
        # this is to update an existing model (the instance argument)
        forum_form = Forum_form(request.POST, instance=forum_being_viewed)
        if forum_form.is_valid():
            forum_form.save()
            return redirect(reverse('show_forum_route', kwargs={
                                        'lesson_id': lesson_id
                                    }))
        else:
            return render(request, 'update_forum.template.html', {
                "form": forum_form,
                "discussion": forum_being_viewed,
                "lesson": lesson_being_viewed
            })
    else:
        # 4. create a form with the book details filled in
        forum_form = Forum_form(instance=forum_being_viewed)
        return render(request, 'update_forum.template.html', {
            "form": forum_form,
            "discussion": forum_being_viewed,
            "lesson": lesson_being_viewed
        })

@login_required    
def delete_forum(request, lesson_id, topic_id):
    forum_being_deleted = get_object_or_404(Forum_topic, pk=topic_id)
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == "POST":
        forum_being_deleted.delete()
        return redirect(reverse('show_forum_route', kwargs={
                                        'lesson_id': lesson_id
                                    }))
    else:
        return render(request, 'delete_forum.template.html', {
            "discussion": forum_being_deleted,
            "lesson": lesson_being_viewed
        })

@login_required
def show_specific_topic(request, topic_id, lesson_id):
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    topic_being_viewed = get_object_or_404(Forum_topic, pk=topic_id)
    return render(request, 'specific_forum_topic.template.html', {
        'discussion': topic_being_viewed,
        'lesson': lesson_being_viewed
        })