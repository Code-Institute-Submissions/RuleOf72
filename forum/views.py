from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from lessons.forms import Lessons_form, Subtopics_form
from lessons.models import Lesson, Sub_topic
from .forms import Forum_form, Comment_form, SearchForm
from .models import Forum_comment, Forum_topic
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q
# Create your views here.

@login_required
def show_forum(request, lesson_id):
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    discussions = Forum_topic.objects.filter(lesson_commented_id=lesson_id)
    if request.GET:
        # always true query:
        queries = ~Q(pk__in=[])

        # if a title is specified, add it to the query
        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            queries = queries & Q(title__icontains=title)

        # update the existing review found
        discussions = discussions.filter(queries)
    search_form = SearchForm(request.GET)
    return render(request, 'forum_topic.template.html', {
        'lesson': lesson_being_viewed,
        'discussions': discussions,
        'search_form': search_form
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
    if request.user == forum_being_viewed.commenter:
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
    else:
        return redirect(reverse('show_forum_route', kwargs={
                                            'lesson_id': lesson_id
                                        }))

@login_required    
def delete_forum(request, lesson_id, topic_id):
    forum_being_deleted = get_object_or_404(Forum_topic, pk=topic_id)
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    if request.user == forum_being_deleted.commenter:
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
    else:
        return redirect(reverse('show_forum_route', kwargs={
                                            'lesson_id': lesson_id
                                        }))

@login_required
def show_specific_topic(request, topic_id, lesson_id):
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    topic_being_viewed = get_object_or_404(Forum_topic, pk=topic_id)
    return render(request, 'specific_forum_topic.template.html', {
        'discussion': topic_being_viewed,
        'lesson': lesson_being_viewed,
        })

@login_required
def create_comment(request, lesson_id, topic_id):
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    topic_being_viewed = get_object_or_404(Forum_topic, pk=topic_id)
    if request.method == "POST":
        form = Comment_form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commenter = request.user
            comment.topic_commented = topic_being_viewed
            comment.save()
            messages.success(request, f"New comment {form.cleaned_data['title']} has been created")
            return redirect(reverse('specific_topic_route', kwargs={
                                        'lesson_id': lesson_id,
                                        'topic_id': topic_id
                                    }))
        else:
            return render(request, 'create_comment.template.html', {
                'form': form,
                'lesson': lesson_being_viewed,
                'topic': topic_being_viewed
            })
    else:
        form = Comment_form()
        return render(request, 'create_comment.template.html', {
            'form': form,
            'lesson': lesson_being_viewed,
            'topic': topic_being_viewed
        })

@login_required
def update_comment(request, lesson_id, topic_id, comment_id):
    # 1. retrieve the book that we are editing
    forum_being_viewed = get_object_or_404(Forum_topic, pk=topic_id)
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    comment_being_viewed = get_object_or_404(Forum_comment, pk=comment_id)
    if request.user == comment_being_viewed.commenter:
    # 2. if the update form is submitted
        if request.method == "POST":

            # 3. create the form and fill in the user's data. Also specify that
            # this is to update an existing model (the instance argument)
            comment_form = Comment_form(request.POST, instance=comment_being_viewed)
            if comment_form.is_valid():
                comment_form.save()
                return redirect(reverse('specific_topic_route', kwargs={
                                            'lesson_id': lesson_id,
                                            'topic_id': topic_id
                                        }))
            else:
                return render(request, 'update_comment.template.html', {
                    "form": comment_form,
                    "discussion": forum_being_viewed,
                    "lesson": lesson_being_viewed,
                    "comment": comment_being_viewed
                })
        else:
            # 4. create a form with the book details filled in
            comment_form = Comment_form(instance=comment_being_viewed)
            return render(request, 'update_comment.template.html', {
                "form": comment_form,
                "discussion": forum_being_viewed,
                "lesson": lesson_being_viewed,
                "comment": comment_being_viewed
            })
    else:
        return redirect(reverse('specific_topic_route', kwargs={
                                            'lesson_id': lesson_id,
                                            'topic_id': topic_id
                                        }))

@login_required    
def delete_comment(request, lesson_id, topic_id, comment_id):
    forum_being_viewed = get_object_or_404(Forum_topic, pk=topic_id)
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    comment_being_viewed = get_object_or_404(Forum_comment, pk=comment_id)
    if request.user == comment_being_viewed.commenter:
        if request.method == "POST":
            comment_being_viewed.delete()
            return redirect(reverse('specific_topic_route', kwargs={
                                            'lesson_id': lesson_id,
                                            'topic_id': topic_id
                                        }))
        else:
            return render(request, 'delete_comment.template.html', {
                "discussion": forum_being_viewed,
                "lesson": lesson_being_viewed,
                "comment": comment_being_viewed
            })
    else:
        return redirect(reverse('specific_topic_route', kwargs={
                                            'lesson_id': lesson_id,
                                            'topic_id': topic_id
                                        })) 