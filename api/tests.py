from django.test import TestCase
import requests
# Create your tests here.
try:
    res = requests.get("http://127.0.0.1:8000/api/")
except (ConnectionError, requests.exceptions.ConnectionError):
    pass
else:
    # print(res.status_code)
    print(res.json())
    # Getting the 1st user
    user = res.json()[0]
    print(user)
    print(user['bank_balance'])
