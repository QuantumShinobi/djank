from django.db import models
import uuid
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=25, unique=True)
    password = models.BinaryField()
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    bank_balance = models.IntegerField(default=100)
    unique_id = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username


class Discord_Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discord_username = models.CharField(
        editable=True, max_length=37, default=None, null=True)
    is_verified = models.BooleanField(default=False, null=False)
    discord_id = models.IntegerField(default=None)
    bot_key = models.CharField(max_length=200, default=None)
