from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('sahiplen/',sahiplenme,name='sahiplenme'),
    path('Acil-durum/',acil_durum,name='acil_durum'),
    path('mama-bagis',mama_sayfasi,name='mama')
]
