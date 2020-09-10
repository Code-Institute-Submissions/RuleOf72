from django.test import TestCase

# Create your tests here.

class TestViews(TestCase):
    def test_get_profiles_page(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles.template.html')