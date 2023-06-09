from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('countries-list/', views.countries_list, name='countries-list'),
    path('countries-list/<str:letter>/', views.countries_letter, name='countries-letter'),
    path('countries-list/letter/<str:state>/', views.one_country, name='country'),
    path('languages/', views.languages_list, name='languages-list'),
    path('languages/<str:language_name>/', views.language_detail, name='language-detail')
]
