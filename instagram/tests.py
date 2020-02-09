from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='charles', password = 'sahara')
        self.user.save()

        self.profile_test = Profile(id=1, name='image', profile_picture='default.jpg', bio='this is a test profile',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)


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
