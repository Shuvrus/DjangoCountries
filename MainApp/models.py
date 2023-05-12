from django.db import models


# FIXME: классы никогда не называются во множественном числе
#   Languages --> Language
class Languages(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


# FIXME: Countries --> Country
class Countries(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(to=Languages)

    def __str__(self):
        return f'{self.name}, {self.languages}'

    def __repr__(self):
        return f'{self.name}, {self.languages}'
