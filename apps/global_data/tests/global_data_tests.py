import unittest

from webtest import TestApp

from app import app


class GlobalDataUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = TestApp(app)

    def test_create_json_file(self):
        response = self.app.post(
            '/api/setGlobalData?username=testuser',
            {'name': '1', 'value': '2'}
        )
        assert response.status_int == 200

    def test_update_json_with_same_name(self):
        response = self.app.post(
            '/api/setGlobalData?username=testuser',
            {'name': '1', 'value': '3'}
        )
        assert response.status_int == 200


if __name__ == '__main__':
    unittest.main( )
