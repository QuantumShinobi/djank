from django.test import TestCase
from .models import User
# Create your tests here.
import bcrypt
import random


class UserTestCase(TestCase):
    uuid = ""

    def setUp(self):
        new_user = User.objects.create()
        new_user.username = "Test User 1"
        passwords = ['hunt', 'fish', 'beg', 'work',
                     'poke2', 'alphanumericallll1235', 'ææhmm']
        self.pwd = random.choice(passwords)
        hash = bcrypt.hashpw(bytes(self.pwd, 'utf-8'), bcrypt.gensalt())
        new_user.password = hash
        self.uuid = new_user.unique_id
        new_user.save()

    def test_overall(self):
        user = User.objects.get(unique_id=self.uuid)
        self.assertEqual(bcrypt.checkpw(
            bytes(self.pwd, 'utf-8'), user.password), True)
