
# Importamos a biblioteca de testes
import unittest
from app import app as application

class TestHello(unittest.TestCase):

    def setUp(self):
        app = application.test_client()
        self.response = app.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_string_response(self):
        self.assertEqual("Hello World !", self.response.data.decode('utf-8'))

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

if __name__ == '__main__':
    unittest.main()