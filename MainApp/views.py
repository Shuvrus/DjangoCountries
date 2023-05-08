from django.shortcuts import render, HttpResponse
import json

with open('countries.json', 'r') as read_file:
    countries = json.load(read_file)


def home(request):
    return render(request, 'index.html')


def countries_list(request):
    context = {'countries': countries}
    return render(request, 'countries-list.html', context)


def one_country(request, country):
    for char in countries:
        if char['country'] == country:
            context = {'country': char}
            return render(request, 'one-country.html', context)


def languages_list(request):
    lang = []
    for char1 in countries:
        for char2 in char1['languages']:
            if char2 in lang:
                continue
            else:
                lang.append(char2)
    lang = sorted(lang)
    context = {'languages': lang}
    return render(request, 'languages.html', context)
