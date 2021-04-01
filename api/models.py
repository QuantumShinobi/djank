from django.db import models

# Create your models here.


class Hero(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=60)
    test_fld = models.BooleanField(default=False)

    def __str__(self):
        return self.name
