import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoCountries.settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
from MainApp.models import Languages, Countries

import json

# with open('countries.json', 'r') as read_file:
#     data = json.load(read_file)
#
# lang = []
# for char1 in data:
#     for char2 in char1['languages']:
#         if char2 in lang:
#             continue
#         else:
#             lang.append(char2)
# lang = sorted(lang)
#
# for char in lang:
#     language = Languages(name=char)
#     language.save()
#
# for char in data:
#     country = Countries(name=char['country'])
#     country.save()
#
# countries = Countries.objects.all()
# languages = Languages.objects.all()
#
# for country in countries:
#     for char in data:
#         if char['country'] == country.name:
#             for lang in char['languages']:
#                 for language in languages:
#                     if language.name == lang:
#                         country.languages.add(language)
