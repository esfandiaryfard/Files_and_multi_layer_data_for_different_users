from webtest import TestApp

import unittest

from app import app


class UploadUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = TestApp(app)

    def test_file_not_exists(self):
        response = self.app.post('/api/upload?username=testuser')
        assert response.status_int == 400

    def test_upload_file(self):
        response = self.app.post(
            '/api/upload?username=testuser',
            [('file', 'apps/upload/tests/test_assests/1217659.png')]
        )
        assert response.status_int == 200


if __name__ == '__main__':
    unittest.main()
