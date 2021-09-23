from django.db import models


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
