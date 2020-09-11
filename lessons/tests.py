from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Lesson
import django.db.utils
# Create your tests here.

class LessonViewTestCase(TestCase):
    

    def test_can_get_create_lesson_form(self):
        response = self.client.get('/lessons/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_lessons.template.html')

    def test_can_create_lesson(self):
        teacher = User.objects.create_user(username='DEF')
        response = self.client.post('/lessons/create/', {
            "topic": "bonds 101",
            "price": 999,
            "teacher": str(teacher.id),
        })
        self.assertEqual(response.status_code, 200)
        print(response.content)
        lesson = Lesson.objects.filter(topic="bonds 101")
        self.assertEqual(lesson.count(), 1)
