from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAppModelTest(TestCase):
    def test_creating_model(self):
        data ={
            'password': 'testpassword',
            'phone_number': '09351234567'
        }

        user = User.objects.create(**data)        

        self.assertEqual(user, User.objects.get(phone_number=data['phone_number']))
