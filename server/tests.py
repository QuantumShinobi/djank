from django.test import TestCase
import os
# Create your tests here.


class TestUser(TestCase):
    def test_env_vars():

        print(os.getenv("GITHUB_WORKFLOW"))
