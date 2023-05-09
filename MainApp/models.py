from django.db import models


class Languages(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class Countries(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(to=Languages)

    def __str__(self):
        return f'{self.name}, {self.languages}'

    def __repr__(self):
        return f'{self.name}, {self.languages}'
