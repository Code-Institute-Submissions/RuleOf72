from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Lesson
import django.db.utils
# Create your tests here.

class CreateLessonViewTestCase(TestCase):
    def test_can_get_animal_form(self):
        response = self.client.get('/lessons/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_lessons.template.html')
