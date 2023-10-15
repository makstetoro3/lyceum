from django.test import TestCase, Client


class StaticURLTest(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_int_endpoint(self):
        response = Client().get("/catalog/12")
        self.assertEqual(response.status_code, 200)

    def test_catalog_no_int_endpoint(self):
        response = Client().get("/catalog/1r")
        self.assertEqual(response.status_code, 404)

    def test_catalog_re_int_endpoint(self):
        response = Client().get("/catalog/re/72")
        self.assertEqual(response.status_code, 200)

    def test_catalog_re_no_int_endpoint(self):
        response = Client().get("/catalog/re/1g")
        self.assertEqual(response.status_code, 404)

    def test_catalog_converter_int_endpoint(self):
        response = Client().get("/catalog/converter/14")
        self.assertEqual(response.status_code, 200)

    def test_catalog_converter_no_int_endpoint(self):
        response = Client().get("/catalog/converter/f2")
        self.assertEqual(response.status_code, 404)

