from django.test import TestCase, Client
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate

# Create your tests here.


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='charles', email = 'test@gmail.com', password = 'sahara')
        self.user.save()

        self.profile_test = Profile(id=1, name='image', profile_picture='default.jpg', bio='this is a test profile',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

    def test_secure_page(self):
        trial = User.objects.all()
        c = Client()
        print(c.login(username='charles', password='sahara'))
        print("*************************")
        response = c.get('/', follow=True)
        print(response)
        print("*******************************")
        user = User.objects.get(username='charles')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.context['email'], 'test@gmail.com')
        # self.assertEqual(response.json()['email'], 'test@gmail.com')


# class TestPost(TestCase):
#     def setUp(self):
#         self.user = User(id=3, username='trial', password = 'sahara')
#         self.user.save()

#         self.profile_test = Profile(id=1, name='image', profile_picture='default.jpg', bio='this is a test profile',user=self.user)
#         self.profile_test.save()

#         self.image_test = Caption(image='default.png', name='test', caption='default test', user=self.profile_test)

#     def test_instance(self):
#         self.assertTrue(isinstance(self.image_test, Caption))

#     def test_save_image(self):
#         self.image_test.save_image()
#         images = Caption.objects.all()
#         self.assertTrue(len(images) > 0)

#     def test_delete_image(self):
#         self.image_test.delete_image()
#         after = Profile.objects.all()
#         self.assertTrue(len(after) < 1)
