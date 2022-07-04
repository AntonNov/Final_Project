from django.test import TestCase
from django.contrib.auth import authenticate, get_user_model


class URLTests(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_tomorrow_page(self):
        response = self.client.get('/tomorrow/')
        self.assertEqual(response.status_code, 200)

    def test_today_page(self):
        response = self.client.get('/today/')
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)


class SigningTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            password='12test12')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
