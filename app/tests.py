from django.test import TestCase, override_settings


class HomePageTests(TestCase):
    @override_settings(DEBUG=False)
    def test_homepage_is_available_when_debug_is_disabled(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Seu próximo deploy')
        self.assertContains(response, 'Docker')
