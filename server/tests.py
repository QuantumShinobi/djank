from django.test import TestCase
import os
# Create your tests here.


class TestUser(TestCase):
    print(os.getenv("GITHUB_WORKFLOW"))
