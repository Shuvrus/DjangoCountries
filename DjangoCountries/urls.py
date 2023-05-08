from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries-list/', views.countries_list),
    path('countries-list/<str:country>/', views.one_country),
    path('languages/', views.languages_list)
]
