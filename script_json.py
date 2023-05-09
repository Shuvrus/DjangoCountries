import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoCountries")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
from MainApp.models import Languages, Countries

import json

with open('countries.json', 'r') as read_file:
    data = json.load(read_file)

lang = []
for char1 in data:
    for char2 in char1['languages']:
        if char2 in lang:
            continue
        else:
            lang.append(char2)
lang = sorted(lang)

for char in lang:
    language = Languages(name=char)
    language.save()
