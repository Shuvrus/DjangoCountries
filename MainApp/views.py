from django.shortcuts import render, HttpResponse
from MainApp.models import Countries, Languages

# FIXME: нужные данные получаем внутри функции-обработчика, а не в качестве глобальной переменной
countries = Countries.objects.all()
languages = Languages.objects.all()


def home(request):
    return render(request, 'index.html')


def countries_list(request):
    # FIXME: нужны данные о странах? Делаем запрос тут
    context = {'countries': countries}
    return render(request, 'countries-list.html', context)


def one_country(request, country):
    # FIXME: плохое именование переменных
    for char in countries:
        # FIXME: получение страны из БД должно быть реализовано на уровне ORM-запроса, а не питоном
        #  Подробнее тут: https://tutorial.djangogirls.org/ru/django_orm/#%D1%84%D0%B8%D0%BB%D1%8C%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2
        #  Или тут: https://metanit.com/python/django/5.13.php

        if char.name == country:
            language = char.languages.all()
            context = {'country': char,
                       'languages': language}
            return render(request, 'one-country.html', context)


def languages_list(request):
    context = {'languages': languages}
    return render(request, 'languages.html', context)

