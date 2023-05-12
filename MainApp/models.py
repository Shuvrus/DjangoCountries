from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class Country(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(to=Language)

    def __str__(self):
        return f'{self.name}, {self.languages}'

    def __repr__(self):
        return f'{self.name}, {self.languages}'
