from django.db import models

# Create your models here.
from datetime import datetime, timezone
from django.db import models
from server.models import User
import uuid
# Create your models here.


class Query(models.Model):
    unique_id = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False)
    unique_id_2 = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False)
    # time_created = models.DateTimeField(default=datetime.now(tz=timezone.utc))
    time_created = models.DateTimeField(auto_now_add=True)

    mail = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f"ID - {self.unique_id}\n TIME - {self.time_created}"
