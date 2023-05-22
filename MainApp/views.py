from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from MainApp.models import Country, Language
import string as st


def home(request):
    return render(request, 'index.html')


def countries_list(request):
    countries = Country.objects.all()
    letters = st.ascii_uppercase
    paginator = Paginator(countries, 10)
    page_number = request.GET.get('page')
    page_countries = paginator.get_page(page_number)
    context = {
        'letters': letters,
        'page_countries': page_countries
    }
    return render(request, 'countries-list.html', context)


def countries_letter(request, letter):
    countries = Country.objects.all()
    letters = st.ascii_uppercase
    country_letter = []
    for country in countries:
        if country.name[0].upper() == letter:
            country_letter.append(country)
    paginator = Paginator(country_letter, 10)
    page_number = request.GET.get('page')
    page_countries = paginator.get_page(page_number)
    context = {
        'letters': letters,
        'page_countries': page_countries
    }
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

