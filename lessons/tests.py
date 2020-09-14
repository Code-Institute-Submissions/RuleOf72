from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Lesson
import django.db.utils
from django.urls import reverse
# Create your tests here.

class LessonViewTestCase(TestCase):
    

    def test_can_get_create_lesson_form(self):
        response = self.client.get('/lessons/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_lessons.template.html')

    def test_can_create_lesson(self):
        teacher = User.objects.create_user(username='DEF')
        teacher.save()
        response = self.client.post('/lessons/create/', {
            "topic": "bonds 101",
            "price": 999,
            "teacher": str(teacher.id),
        })
        self.assertEqual(response.status_code, 200)
        lesson = Lesson.objects.filter(topic="bonds 101")
        self.assertEqual(lesson.count(), 1)

    def test_can_get_update_lesson_form(self):
        teacher = User.objects.create_user(username='EFG')
        teacher.save()
        lesson = Lesson(topic='CFD', price=999, teacher=teacher)
        lesson.save()
        response = self.client.get(f'/lessons/update/{lesson.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_lessons.template.html')

    def test_can_update_lesson(self):
        teacher = User.objects.create_user(username='EFG')
        teacher.save()
        teacher2 = User.objects.create_user(username='ZZZ')
        teacher2.save()
        lesson = Lesson(topic='CFD', price=999, teacher=teacher)
        lesson.save()
        response = self.client.post(reverse('update_lesson_route', kwargs={'lesson_id': str(lesson.id)}), {
            'topic': 'CFD2',
            'price': 888,
            'teacher': str(teacher2.id)
        })
        self.assertEqual(response.status_code, 302)
        update_lesson = get_object_or_404(Lesson, pk=lesson.id)
        self.assertEquals(update_lesson.topic, "CFD2")
        self.assertEquals(update_lesson.price, 888)
        self.assertEquals(update_lesson.teacher, teacher2)

    def test_can_get_delete_page(self):
        teacher = User.objects.create_user(username='ZZZ')
        teacher.save()
        lesson = Lesson(topic='CFD', price=999, teacher=teacher)
        lesson.save()
        response = self.client.get(f'/lessons/delete/{lesson.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_lessons.template.html')