from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from .forms import Lessons_form, Subtopics_form, SearchForm
from .models import Lesson, Sub_topic
from purchases.models import Purchase
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage

# Create your views here.

@login_required
def all_lessons(request):
    all_lessons = Lesson.objects.all()
    if request.GET:
        # always true query:
        queries = ~Q(pk__in=[])

        # if a title is specified, add it to the query
        if 'topic' in request.GET and request.GET['topic']:
            topic = request.GET['topic']
            queries = queries & Q(topic__icontains=topic)

        # update the existing review found
        all_lessons = all_lessons.filter(queries)
    search_form = SearchForm(request.GET)
    return render(request, "lessons/all_lessons.template.html", {
        'all_lessons': all_lessons,
        'search_form': search_form,
    })


# Paginator not working
# @login_required
# def all_lessons(request):
#     all_lessons = Lesson.objects.all()
#     if request.GET:
#         # always true query:
#         queries = ~Q(pk__in=[])

#         # if a title is specified, add it to the query
#         if 'topic' in request.GET and request.GET['topic']:
#             topic = request.GET['topic']
#             queries = queries & Q(topic__icontains=topic)

#         # update the existing review found
#         all_lessons = all_lessons.filter(queries)
#     p = Paginator(all_lessons, 4)
#     page_num = request.GET.get('page', 1)
#     try:
#         page = p.page(page_num)
#     except EmptyPage:
#         page = p.page(1)
#     context = {'items': page}
#     search_form = SearchForm(request.GET)
#     return render(request, "lessons/all_lessons.template.html", context, {
#         'search_form': search_form,
#     })

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
            return render(request, 'lessons/create_lessons.template.html', {
                'form': form
            })
    else:
        form = Lessons_form()
        return render(request, 'lessons/create_lessons.template.html', {
            'form': form
        })

@login_required
def update_lesson(request, lesson_id):
    # 1. retrieve the book that we are editing
    lesson_being_updated = get_object_or_404(Lesson, pk=lesson_id)
    if request.user == lesson_being_updated.teacher:
    # 2. if the update form is submitted
        if request.method == "POST":

            # 3. create the form and fill in the user's data. Also specify that
            # this is to update an existing model (the instance argument)
            lesson_form = Lessons_form(request.POST, instance=lesson_being_updated)
            if lesson_form.is_valid():
                lesson_form.save()
                return redirect(reverse(all_lessons))
            else:
                return render(request, 'lessons/update_lessons.template.html', {
                    "form": lesson_form
                })
        else:
            # 4. create a form with the book details filled in
            lesson_form = Lessons_form(instance=lesson_being_updated)
            return render(request, 'lessons/update_lessons.template.html', {
                "form": lesson_form
            })
    
    else:
        return redirect(reverse(all_lessons))

@login_required    
def delete_lesson(request, lesson_id):
    lesson_being_deleted = get_object_or_404(Lesson, pk=lesson_id)
    if request.user == lesson_being_deleted.teacher:
        if request.method == "POST":
            lesson_being_deleted.delete()
            return redirect(reverse(all_lessons))
        else:
            return render(request, 'lessons/delete_lessons.template.html', {
                "lesson": lesson_being_deleted
            })
    else:
        return redirect(reverse(all_lessons))

def specific_lesson(request, lesson_id):
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessons/specific_lessons.template.html', {
        'lesson': lesson_being_viewed
    })

@login_required
def add_sub_topic(request, lesson_id):
    form = Subtopics_form(request.POST)
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    if request.user == lesson_being_viewed.teacher:
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
                return render(request, 'lessons/add_sub_topic.template.html', {
                    'form': form,
                    'lesson': lesson_being_viewed
                })
        else:
            form = Subtopics_form()
            return render(request, 'lessons/add_sub_topic.template.html', {
                'form': form,
                'lesson': lesson_being_viewed
            })
    else:
        return redirect(reverse('lessons/specific_lesson_route',
                                        kwargs={
                                            'lesson_id': lesson_id
                                        }))
@login_required
def update_sub_topic(request, lesson_id, sub_topic_id):
    # 1. retrieve the book that we are editing
    topic_being_updated = get_object_or_404(Sub_topic, pk=sub_topic_id)
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    # 2. if the update form is submitted
    sub_topic_form = Subtopics_form(request.POST, instance=topic_being_updated)
    if request.user == lesson_being_viewed.teacher:
        if request.method == "POST":
            if sub_topic_form.is_valid():
                sub_topic_form.save()
                return redirect(reverse('lessons/specific_lesson_route',
                                        kwargs={
                                            'lesson_id': lesson_id
                                        }))
            else:
                return render(request, 'lessons/update_sub_topic.template.html', {
                    "form": sub_topic_form,
                    "lesson": lesson_being_viewed,
                    "sub_topic": topic_being_updated
                })
        else:
            # 4. create a form with the book details filled in
            sub_topic_form = Subtopics_form(instance=topic_being_updated)
            return render(request, 'lessons/update_sub_topic.template.html', {
                "form": sub_topic_form,
                'sub_topic': topic_being_updated,
                "lesson": lesson_being_viewed
            })
    else:
        return redirect(reverse('lessons/specific_lesson_route',
                                        kwargs={
                                            'lesson_id': lesson_id
                                        }))

@login_required
def delete_sub_topic(request, lesson_id, sub_topic_id):
    topic_being_deleted = get_object_or_404(Sub_topic, pk=sub_topic_id)
    lesson_being_viewed = get_object_or_404(Lesson, pk=lesson_id)
    if request.user == lesson_being_viewed.teacher:
        if request.method == "POST":
            topic_being_deleted.delete()
            return redirect(reverse('lessons/specific_lesson_route',
                                        kwargs={
                                            'lesson_id': lesson_id,
                                            'sub_topic_id': sub_topic_id
                                        }))
        else:
            return render(request, 'lessons/delete_sub_topic.template.html', {
                "sub_topic": topic_being_deleted,
                "lesson": lesson_being_viewed
            })
    else:
        return redirect(reverse('lessons/specific_lesson_route',
                                        kwargs={
                                            'lesson_id': lesson_id,
                                            'sub_topic_id': sub_topic_id
                                        }))

@login_required
def created_lessons(request):
    all_lessons = Lesson.objects.filter(teacher=request.user)
    return render(request, "lessons/created_lessons.template.html", {
        'all_lessons': all_lessons
    })

@login_required
def purchased_lessons(request):
    lesson = Lesson.objects.filter().prefetch_related('purchased')
    return render(request, "lessons/purchased_lessons.template.html", {
        'lessons': lesson
    })