from django.shortcuts import render, HttpResponse
from MainApp.models import Countries, Languages

countries = Countries.objects.all()
languages = Languages.objects.all()


def home(request):
    return render(request, 'index.html')


def countries_list(request):
    context = {'countries': countries}
    return render(request, 'countries-list.html', context)


def one_country(request, country):
    for char in countries:
        if char.name == country:
            language = char.languages.all()
            context = {'country': char,
                       'languages': language}
            return render(request, 'one-country.html', context)


def languages_list(request):
    context = {'languages': languages}
    return render(request, 'languages.html', context)

