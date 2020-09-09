from django.test import TestCase
from django.shortcuts import get_object_or_404

from .models import lessons, User
from .forms import lessonsForm
import django.db.utils
# Create your tests here.

class lessonsModelTestCase(TestCase):

    def test_create_lesson_model(self):

        u = User(first_name="Tan", last_name="Ah Kow",
                username="ahkowtan", email="t@t.com",
                date_joined=)
        u.save()

        l = lessons()
        l.topic = "stocks"
        l.price = 9.9
        l.date_joined = 
        l.user = u

        l.save()

        self.assertTrue(l.id > 0)
        lesson = get_object_or_404(lessons, pk=l.id)
        self.assertTrue(lesson is not None)

        self.assertEqual(lesson.topic, "stocks")
        self.assertEqual(lesson.price, 9.9)
        self.assertEqual(lesson.date_joined, )
        self.assertEqual(lesson.user, u)
