from django.db import models
import uuid
import bcrypt
from django.shortcuts import render


class User(models.Model):
    username = models.CharField(max_length=25, unique=True)
    password = models.BinaryField(editable=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    bank_balance = models.IntegerField(default=100)
    unique_id = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username

    def authenticate(self, pwd, request, bot=False):
        if bot == False:
            if bcrypt.checkpw(bytes(pwd, 'utf-8'), self.password):
                response = render(request, 'main/logout.html',
                                  context={"title": "Login",
                                           "text": "Logging you in"})
                response.set_cookie(
                    "user-identity", str(self.unique_id), max_age=31104000)
                return response
            if type(self.password) == memoryview:
                if bcrypt.checkpw(bytes(pwd, 'utf-8'), self.password.tobytes()):

                    response = render(request, 'main/logout.html',
                                      context={"title": "Login",
                                               "text": "Logging you in"})
                    response.set_cookie("user-identity", str(self.unique_id))
                    return response
                else:
                    return render(request, "main/login.html", context={"error": "Password is incorrect"})
            else:
                if bcrypt.checkpw(bytes(pwd, 'utf-8'), self.password):
                    response = render(request, 'main/logout.html',
                                      context={"title": "Login",
                                               "text": "Logging you in"})
                    response.set_cookie("user-identity", str(self.unique_id))
                    return response
                else:
                    return render(request, "main/login.html", context={"error": "Password is incorrect"})
        elif bot == True:
            return bcrypt.checkpw(bytes(pwd, 'utf-8'), bytes(self.password, 'utf-8'))


class Discord_Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discord_username = models.CharField(
        editable=True, max_length=37, default=None, null=False)
    is_verified = models.BooleanField(default=False, null=False, editable=True)
    discord_id = models.IntegerField(default=None, null=True)
