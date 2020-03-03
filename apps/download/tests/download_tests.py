import unittest

from webtest import TestApp

from app import app


class DownloadUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = TestApp(app)

    def test_download_file(self):
        response = self.app.get(
            '/api/download?username=testuser&filename=1217659.png'
        )
        assert response.status_int == 200


if __name__ == '__main__':
    unittest.main()
