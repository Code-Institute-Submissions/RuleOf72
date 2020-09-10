from django.test import TestCase

# Create your tests here.

class TestViews(TestCase):
    def test_get_forum_page(self):
        response = self.client.get('/forum/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum.template.html')