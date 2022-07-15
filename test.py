from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self) # used to create a test mocking up the functionality of current app
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self) # used to create a test mocking up the functionality of current app
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    # Ensure login behaves correctly given correct credentials


    # Ensure login behaves correctly given incorrect credentials


    # Ensure logout behaves correctly

if __name__ == '__main__':
    unittest.main()