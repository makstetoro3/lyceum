from django.test import TestCase, Client


class StaticURLTest(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)
