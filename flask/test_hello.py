import unittest
from hello import app

class TestHello(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Index Page")

    def test_show_subpath(self):
        response = self.app.get('/path/foo/bar')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Subpath foo/bar")

    def test_show_subpath_invalid(self):
        response = self.app.get('/path/<script>alert(1)</script>')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
