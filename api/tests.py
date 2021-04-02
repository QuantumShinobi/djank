from django.test import TestCase
import requests
# Create your tests here.
# Testing GET request
# try:
#     res = requests.get("http://127.0.0.1:8000/api/")
# except (ConnectionError, requests.exceptions.ConnectionError):
#     pass
# else:
#      print(res.status_code)
#     print(res.json())
#     # Getting the 1st user
#     user = res.json()[0]
#     print(user)
# print(user['bank_balance'1])

# POST req
url = "http://127.0.0.1:8000/api/discord"
data = {"username": "rishit", "discord_username": "IamEinstein#4444",
        "discord_id": 0000, "bot_key": "API", "password": "okay"}
response = requests.post(url, data=data)
print(response.json())
