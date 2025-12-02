import src
import json
import unittest
from src.response_codes import HttpCodes


class TestRoot(unittest.TestCase):
    def setUp(self):
        app = src.create_flask_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def test_root(self):
        response = self.app.get(
            "/",
            follow_redirects=True
        )
        self.assertEqual(response.status_code, HttpCodes.HTTP_200_OK)
        data = json.loads(response.data.decode())
        expected_data = "Hello Root Endpoint!"
        self.assertEqual(data, expected_data)
