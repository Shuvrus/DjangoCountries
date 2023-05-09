from django.db import models


class Languages(models.Model):
    name = models.CharField(max_length=50)


class Countries(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(to=Languages)
