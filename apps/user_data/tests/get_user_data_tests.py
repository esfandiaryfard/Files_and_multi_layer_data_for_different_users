import unittest

from webtest import TestApp

from app import app


class GetUserDataUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = TestApp(app)

    def test_get_user_json_file(self):
        response = self.app.get('/api/getUserData?username=testuser')
        assert response.status_int == 200


if __name__ == '__main__':
    unittest.main( )
