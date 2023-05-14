from django.shortcuts import render, HttpResponse
from MainApp.models import Country, Language


def home(request):
    return render(request, 'index.html')


def countries_list(request):
    countries = Country.objects.all()
    context = {'countries': countries}
    return render(request, 'countries-list.html', context)


def one_country(request, state):
    country = Country.objects.get(name=state)
    languages = country.languages.all()
    context = {'country': country,
               'languages': languages}
    return render(request, 'one-country.html', context)


def languages_list(request):
    languages = Language.objects.all()
    context = {'languages': languages}
    return render(request, 'languages.html', context)


def language_detail(request, language_name):
    countries = Country.objects.filter(languages__name=language_name)
    context = {
        'language': language_name,
        'countries': countries
    }
    return render(request, 'language-detail.html', context)

