from django.db import models
import uuid
# Create your models here.


class Redirect(models.Model):
    link1 = models.CharField(max_length=10485700)
    unique_id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False)
    link2 = models.CharField(
        max_length=10485700, editable=True, null=True, default=None)
    link3 = models.CharField(
        max_length=10485700, editable=True, null=True, default=None)
    link4 = models.CharField(
        max_length=10485700, editable=True, null=True, default=None)
    link5 = models.CharField(
        max_length=10485700, editable=True, null=True, default=None)
    link6 = models.CharField(
        max_length=10485700, editable=True, null=True, default=None)
    link7 = models.CharField(
        max_length=10485700, editable=True, null=True, default=None)
    link8 = models.CharField(
        max_length=10485700, editable=True, null=True, default=None)
    link9 = models.CharField(
        max_length=10485700, editable=True, null=True, default=None)
    link10 = models.CharField(
        max_length=10485700, editable=True, null=True, default=None)


class RedirectLink(models.Model):
    link = models.CharField(max_length=10485700)
    unique_id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False)
    url = models.CharField(max_length=10485700, null=True)
    url2 = models.CharField(max_length=10485700, null=True)

    def get_url(self, request=None):
        host = request.META['HTTP_HOST']
        self.url = f"http://{host}/r/{self.unique_id}"
        self.save()
        return self.url

    def get_url2(self):
        self.url2 = f"http://djank.herokuapp.com/r/{self.unique_id}"
        self.save()
        return self.url2




class ProtectLink(models.Model):
    link = models.CharField(max_length=10485700)
    password = models.UUIDField(default=uuid.uuid4(), null=False, editable=False)
    