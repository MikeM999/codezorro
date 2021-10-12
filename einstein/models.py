from django.db import models
from django.db.models.fields import UUIDField


class Language(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Topic(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Narrative(models.Model):
    code = models.CharField(max_length=4)
    text = models.TextField()

    def __str__(self):
        return self.text[0:40]


class Xmail(models.Model):
    name = models.CharField(max_length=60, null=False)
    email = models.EmailField(max_length=95, null=False)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
