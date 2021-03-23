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
